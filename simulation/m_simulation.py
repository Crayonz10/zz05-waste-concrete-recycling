#!/usr/bin/env python3
"""
Numerical simulation for waste concrete recycling biform game
Exploring the impact of m (recycler's processing cost) on equilibrium outcomes
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set up Nature-style font and parameters
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['figure.dpi'] = 300

# Nature-inspired Morandi color palette
COLORS = {
    'M': '#5B8C5A',  # Sage green
    'R': '#A17D74',  # Dusty rose/mauve
}

def calculate_equilibrium(alpha, beta, s, w, m, mu_M, mu_R, c, theta):
    """
    Calculate equilibrium values for given parameters.
    """
    # Common denominator
    D = ((alpha - beta)**3 * (alpha + beta) * theta**4
         - 4 * c * (alpha - beta) * (3*alpha**2 - beta**2) * theta**2
         + 4 * c**2 * (4*alpha**2 - beta**2))

    # p_M* numerator
    N_pM = (4 * c**2 * (2*alpha**2*(s - w - mu_M) + alpha*beta*(s - m - mu_R) - beta**2*(w - m))
             - 2 * c * theta**2 * ((alpha - beta) * (alpha**2*(s - w - mu_M) - (alpha**2 - alpha*beta + beta**2)*(w - m))
                                    - alpha * (alpha**2 - alpha*beta + beta**2) * (mu_M - mu_R)))

    # p_R* numerator
    N_pR = (4 * c**2 * alpha * (2*alpha*(s - m - mu_R) + beta*(s - 3*w + 2*m - mu_M))
             - 2 * c * alpha * theta**2 * ((alpha - beta) * (alpha*(w - m) + beta*(s - 3*w + 2*m - mu_M))
                                            + alpha * (alpha - 2*beta) * (mu_M - mu_R)))

    p_M = N_pM / D
    p_R = N_pR / D

    # q_M* numerator
    N_qM = (2 * c * (alpha * (s - w - mu_M) * (2*c*(2*alpha**2 - beta**2) - theta**2*(2*alpha - beta)*(alpha**2 - beta**2))
                      - (alpha*(s - m - mu_R) - beta*(w - m)) * (2*c*alpha*beta - theta**2*alpha*(alpha**2 - beta**2))))

    # q_R* numerator
    N_qR = (2 * c * ((alpha*(s - m - mu_R) - beta*(w - m)) * (2*c*(2*alpha**2 - beta**2) - theta**2*(alpha - beta)*(alpha**2 - beta**2))
                      - alpha*(s - w - mu_M) * (2*c*alpha*beta - theta**2*(alpha - beta)*(alpha**2 - beta**2))))

    q_M = N_qM / D
    q_R = N_qR / D

    # n* calculation
    q_M_direct = alpha * p_M - beta * p_R  # collection quantity of M
    q_R_direct = alpha * p_R - beta * p_M  # collection quantity of R

    n = (2 * q_R_direct**2 + 2 * q_M_direct * q_R_direct - q_M_direct**2) / (2 * ((alpha - beta)*(p_M + p_R))**2)

    # k* calculation (conversion rate)
    k = theta * (alpha - beta) * (p_M + p_R) / c

    # phi_M* and phi_R* calculations
    phi_M = ((s - p_M - w - mu_M) * q_M_direct
             + theta**2 * q_M_direct * (q_M_direct + 2*q_R_direct) / (4*c))

    phi_R = ((s - p_R - m - mu_R) * q_R_direct
             + (w - m) * q_M_direct
             + theta**2 * (q_R_direct**2 + (q_M_direct + q_R_direct)**2) / (4*c))

    return {
        'p_M': p_M,
        'p_R': p_R,
        'q_M': q_M,
        'q_R': q_R,
        'q_total': q_M + q_R,
        'n': n,
        'k': k,
        'phi_M': phi_M,
        'phi_R': phi_R
    }


def main():
    # Fixed parameter values
    alpha = 1.5
    beta = 0.134
    s = 87.5
    w = 35
    mu_M = 25
    mu_R = 44
    c = 135000
    theta = 137.5

    # Range of m values (x-axis) - recycler's processing cost
    m_values = np.linspace(10, 100, 100)

    # Store results
    results = {
        'p_M': [], 'p_R': [],
        'q_M': [], 'q_R': [], 'q_total': [],
        'n': [], 'k': [],
        'phi_M': [], 'phi_R': []
    }

    for m in m_values:
        eq = calculate_equilibrium(alpha, beta, s, w, m, mu_M, mu_R, c, theta)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['n'].append(eq['n'])
        results['k'].append(eq['k'])
        results['phi_M'].append(eq['phi_M'])
        results['phi_R'].append(eq['phi_R'])

    # Filter values - ensure n* is non-negative and prices are positive for valid interpretation
    valid_mask = (np.array(results['n']) >= 0) & (np.array(results['p_M']) > 0) & (np.array(results['p_R']) > 0)
    m_valid = m_values[valid_mask]
    results['p_M'] = np.array(results['p_M'])[valid_mask]
    results['p_R'] = np.array(results['p_R'])[valid_mask]
    results['q_M'] = np.array(results['q_M'])[valid_mask]
    results['q_R'] = np.array(results['q_R'])[valid_mask]
    results['q_total'] = np.array(results['q_total'])[valid_mask]
    results['n'] = np.array(results['n'])[valid_mask]
    results['k'] = np.array(results['k'])[valid_mask]
    results['phi_M'] = np.array(results['phi_M'])[valid_mask]
    results['phi_R'] = np.array(results['phi_R'])[valid_mask]

    # Create figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(8, 7))
    fig.suptitle('Fig. 5. Impact of Processing Cost ($m$) on Equilibrium Outcomes',
                 fontsize=12, fontweight='bold', y=0.98)

    # Plot 1: Collection Prices
    ax1 = axes[0, 0]
    ax1.plot(m_valid, results['p_M'], color=COLORS['M'], label='Manufacturer (M)', linewidth=1.8)
    ax1.plot(m_valid, results['p_R'], color=COLORS['R'], label='Recycler (R)', linewidth=1.8)
    ax1.set_xlabel('Processing Cost ($m$, yuan/m$^3$)')
    ax1.set_ylabel('Collection Price (yuan/m$^3$)')
    ax1.legend(loc='best', frameon=True, fancybox=False, edgecolor='gray', framealpha=0.9)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.set_xlim([m_valid[0], m_valid[-1]])
    ax1.text(0.02, -0.12, 'Fig.5(a)', transform=ax1.transAxes, fontsize=10, fontweight='bold')

    # Plot 2: Collection Quantities
    ax2 = axes[0, 1]
    ax2.plot(m_valid, results['q_M'], color=COLORS['M'], label='Manufacturer (M)', linewidth=1.8)
    ax2.plot(m_valid, results['q_R'], color=COLORS['R'], label='Recycler (R)', linewidth=1.8)
    ax2.plot(m_valid, results['q_total'], color='#6B7B8C', label='Total (Q)', linewidth=1.8, linestyle='--')
    ax2.set_xlabel('Processing Cost ($m$, yuan/m$^3$)')
    ax2.set_ylabel('Collection Quantity (m$^3$)')
    ax2.legend(loc='best', frameon=True, fancybox=False, edgecolor='gray', framealpha=0.9)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.set_xlim([m_valid[0], m_valid[-1]])
    ax2.text(0.02, -0.12, 'Fig.5(b)', transform=ax2.transAxes, fontsize=10, fontweight='bold')

    # Plot 3: Cost-sharing Ratio (n*) and Conversion Rate (k*)
    ax3 = axes[1, 0]
    ax3.plot(m_valid, results['n'], color='#6B7B8C', label='Cost-sharing Ratio ($n^*$)', linewidth=1.8)
    ax3.plot(m_valid, results['k'], color='#8B7355', label='Conversion Rate ($k^*$)', linewidth=1.8)
    ax3.set_xlabel('Processing Cost ($m$, yuan/m$^3$)')
    ax3.set_ylabel('Value')
    ax3.legend(loc='best', frameon=True, fancybox=False, edgecolor='gray', framealpha=0.9)
    ax3.grid(True, alpha=0.3, linestyle='--')
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.set_xlim([m_valid[0], m_valid[-1]])
    ax3.text(0.02, -0.12, 'Fig.5(c)', transform=ax3.transAxes, fontsize=10, fontweight='bold')

    # Plot 4: Profits
    ax4 = axes[1, 1]
    ax4.plot(m_valid, results['phi_M'], color=COLORS['M'], label='Manufacturer (M)', linewidth=1.8)
    ax4.plot(m_valid, results['phi_R'], color=COLORS['R'], label='Recycler (R)', linewidth=1.8)
    ax4.set_xlabel('Processing Cost ($m$, yuan/m$^3$)')
    ax4.set_ylabel('Profit (yuan)')
    ax4.legend(loc='best', frameon=True, fancybox=False, edgecolor='gray', framealpha=0.9)
    ax4.grid(True, alpha=0.3, linestyle='--')
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.set_xlim([m_valid[0], m_valid[-1]])
    ax4.text(0.02, -0.12, 'Fig.5(d)', transform=ax4.transAxes, fontsize=10, fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Save figure
    fig.savefig('simulation/m_impact.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('simulation/m_impact.pdf', bbox_inches='tight', facecolor='white')
    print("Figures saved: m_impact.png, m_impact.pdf")

    # Print summary statistics
    print("\n=== Summary Statistics ===")
    print(f"m range: {m_valid[0]:.2f} to {m_valid[-1]:.2f}")
    print(f"\nAt m = {m_valid[0]:.2f}:")
    print(f"  p_M* = {results['p_M'][0]:.2f}, p_R* = {results['p_R'][0]:.2f}")
    print(f"  q_M* = {results['q_M'][0]:.2f}, q_R* = {results['q_R'][0]:.2f}, q_total* = {results['q_total'][0]:.2f}")
    print(f"  n* = {results['n'][0]:.4f}, k* = {results['k'][0]:.4f}")
    print(f"  φ_M* = {results['phi_M'][0]:.2f}, φ_R* = {results['phi_R'][0]:.2f}")

    print(f"\nAt m = {m_valid[-1]:.2f}:")
    print(f"  p_M* = {results['p_M'][-1]:.2f}, p_R* = {results['p_R'][-1]:.2f}")
    print(f"  q_M* = {results['q_M'][-1]:.2f}, q_R* = {results['q_R'][-1]:.2f}, q_total* = {results['q_total'][-1]:.2f}")
    print(f"  n* = {results['n'][-1]:.4f}, k* = {results['k'][-1]:.4f}")
    print(f"  φ_M* = {results['phi_M'][-1]:.2f}, φ_R* = {results['phi_R'][-1]:.2f}")

    plt.show()


if __name__ == "__main__":
    main()
