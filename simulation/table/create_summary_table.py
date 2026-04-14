#!/usr/bin/env python3
"""
Create summary table of all simulation results
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.patches as mpatches

# Set up matplotlib for table
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 10

def calculate_equilibrium(alpha, beta, s, w, m, mu_M, mu_R, c, theta):
    """Calculate equilibrium values for given parameters."""
    D = ((alpha - beta)**3 * (alpha + beta) * theta**4
         - 4 * c * (alpha - beta) * (3*alpha**2 - beta**2) * theta**2
         + 4 * c**2 * (4*alpha**2 - beta**2))

    N_pM = (4 * c**2 * (2*alpha**2*(s - w - mu_M) + alpha*beta*(s - m - mu_R) - beta**2*(w - m))
             - 2 * c * theta**2 * ((alpha - beta) * (alpha**2*(s - w - mu_M) - (alpha**2 - alpha*beta + beta**2)*(w - m))
                                    - alpha * (alpha**2 - alpha*beta + beta**2) * (mu_M - mu_R)))

    N_pR = (4 * c**2 * alpha * (2*alpha*(s - m - mu_R) + beta*(s - 3*w + 2*m - mu_M))
             - 2 * c * alpha * theta**2 * ((alpha - beta) * (alpha*(w - m) + beta*(s - 3*w + 2*m - mu_M))
                                            + alpha * (alpha - 2*beta) * (mu_M - mu_R)))

    p_M = N_pM / D
    p_R = N_pR / D

    N_qM = (2 * c * (alpha * (s - w - mu_M) * (2*c*(2*alpha**2 - beta**2) - theta**2*(2*alpha - beta)*(alpha**2 - beta**2))
                      - (alpha*(s - m - mu_R) - beta*(w - m)) * (2*c*alpha*beta - theta**2*alpha*(alpha**2 - beta**2))))

    N_qR = (2 * c * ((alpha*(s - m - mu_R) - beta*(w - m)) * (2*c*(2*alpha**2 - beta**2) - theta**2*(alpha - beta)*(alpha**2 - beta**2))
                      - alpha*(s - w - mu_M) * (2*c*alpha*beta - theta**2*(alpha - beta)*(alpha**2 - beta**2))))

    q_M = N_qM / D
    q_R = N_qR / D

    q_M_direct = alpha * p_M - beta * p_R
    q_R_direct = alpha * p_R - beta * p_M

    n = (2 * q_R_direct**2 + 2 * q_M_direct * q_R_direct - q_M_direct**2) / (2 * ((alpha - beta)*(p_M + p_R))**2)
    k = theta * (alpha - beta) * (p_M + p_R) / c

    phi_M = ((s - p_M - w - mu_M) * q_M_direct
             + theta**2 * q_M_direct * (q_M_direct + 2*q_R_direct) / (4*c))

    phi_R = ((s - p_R - m - mu_R) * q_R_direct
             + (w - m) * q_M_direct
             + theta**2 * (q_R_direct**2 + (q_M_direct + q_R_direct)**2) / (4*c))

    return {
        'p_M': p_M, 'p_R': p_R,
        'q_M': q_M, 'q_R': q_R, 'q_total': q_M + q_R,
        'n': n, 'k': k,
        'phi_M': phi_M, 'phi_R': phi_R
    }


def run_simulation(param_name, param_range, fixed_params, varying_param):
    """Run simulation for a parameter."""
    results = []
    for val in param_range:
        params = fixed_params.copy()
        params[varying_param] = val
        eq = calculate_equilibrium(**params)

        # Filter valid results
        if eq['n'] >= 0 and eq['p_M'] > 0 and eq['p_R'] > 0:
            results.append({
                'param_value': val,
                **{k: v for k, v in eq.items()}
            })

    if results:
        return results[0], results[-1]
    return None, None


def main():
    # Fixed base parameters
    base_params = {
        'alpha': 1.5, 'beta': 0.134, 's': 87.5, 'w': 35, 'm': 32,
        'mu_M': 25, 'mu_R': 44, 'c': 135000, 'theta': 137.5
    }

    simulations = [
        ('α (price sensitivity)', 'alpha', np.linspace(0.889, 3.0, 100)),
        ('β (competition intensity)', 'beta', np.linspace(0.01, 0.28, 100)),
        ('s (government subsidy)', 's', np.linspace(85, 200, 100)),
        ('θ (technology)', 'theta', np.linspace(50, 300, 100)),
        ('m (processing cost)', 'm', np.linspace(10, 33, 100)),
        ('w (transfer price)', 'w', np.linspace(28, 60, 100)),
        ('μ_M (M transport cost)', 'mu_M', np.linspace(20, 53, 100)),
        ('μ_R (R transport cost)', 'mu_R', np.linspace(10, 45, 100)),
    ]

    # Collect data
    table_data = []
    for name, param, range_vals in simulations:
        low, high = run_simulation(name, range_vals, base_params.copy(), param)
        if low and high:
            table_data.append({
                'Parameter': name,
                'Range': f'{low["param_value"]:.2f} - {high["param_value"]:.2f}',
                'p_M*': f'{low["p_M"]:.2f} → {high["p_M"]:.2f}',
                'p_R*': f'{low["p_R"]:.2f} → {high["p_R"]:.2f}',
                'q_M*': f'{low["q_M"]:.2f} → {high["q_M"]:.2f}',
                'q_R*': f'{low["q_R"]:.2f} → {high["q_R"]:.2f}',
                'q_total*': f'{low["q_total"]:.2f} → {high["q_total"]:.2f}',
                'n*': f'{low["n"]:.4f} → {high["n"]:.4f}',
                'k*': f'{low["k"]:.4f} → {high["k"]:.4f}',
                'φ_M*': f'{low["phi_M"]:.2f} → {high["phi_M"]:.2f}',
                'φ_R*': f'{low["phi_R"]:.2f} → {high["phi_R"]:.2f}',
            })

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('off')

    # Table data
    columns = ['Parameter', 'Range', 'p_M*', 'p_R*', 'q_M*', 'q_R*', 'q_total*', 'n*', 'k*', 'φ_M*', 'φ_R*']
    cell_text = [[row[col] for col in columns] for row in table_data]

    # Create table
    table = ax.table(
        cellText=cell_text,
        colLabels=columns,
        cellLoc='center',
        loc='center',
        colColours=['#E8E8E8'] * len(columns)
    )

    # Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.8)

    # Style header
    for i in range(len(columns)):
        table[(0, i)].set_text_props(weight='bold')

    # Alternate row colors
    for i in range(1, len(table_data) + 1):
        for j in range(len(columns)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#F5F5F5')
            else:
                table[(i, j)].set_facecolor('#FFFFFF')

    # Set column widths
    col_widths = [0.12, 0.10, 0.09, 0.09, 0.09, 0.09, 0.10, 0.08, 0.08, 0.10, 0.10]
    for i, width in enumerate(col_widths):
        table.auto_set_column_width([i])

    plt.title('Summary of Numerical Simulation Results\n(Arrows indicate direction of change: low → high parameter value)',
              fontsize=12, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('simulation/table/summary_table.pdf', bbox_inches='tight', dpi=300, facecolor='white')
    plt.savefig('simulation/table/summary_table.png', bbox_inches='tight', dpi=300, facecolor='white')
    print("Table saved: simulation/table/summary_table.pdf")
    print("Table saved: simulation/table/summary_table.png")


if __name__ == "__main__":
    main()
