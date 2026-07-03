"""
Plotting code for biform game analysis figures
Using Morandi colors, Nature-style aesthetics
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from equilibria import (
    calc_prices_N, calc_prices_C,
    calc_k_N, calc_k_C, calc_n_C,
    calc_phi_M, calc_phi_R,
)

# Base directory
BASE_DIR = '/Users/zz/Library/CloudStorage/Dropbox/何门撸铁/_gym paper/zz05_合作非合作博弈/zz05_latexfile_RCR'
FIGURE_DIR = os.path.join(BASE_DIR, 'simulation', 'new_figures')

# Ensure figure directory exists
os.makedirs(FIGURE_DIR, exist_ok=True)

# Set up Morandi color palette
MORANDI_COLORS = {
    'blue': '#5B8C85',      # Morandi blue
    'green': '#8FA68A',     # Morandi green
    'red': '#C88D82',       # Morandi red
    'purple': '#9B8AA0',    # Morandi purple
    'orange': '#D4A574',    # Morandi orange
}

# Set matplotlib global style
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'axes.linewidth': 1.2,
    'lines.linewidth': 2.0,
    'axes.grid': False,
})

# Base parameters (adjusted for positive values and crossover)
BASE_PARAMS = {
    'alpha': 1.5,
    'beta': 0.134,
    'm': 32,
    'w': 35,
    's': 87.5,
    'mu_M': 25,
    'mu_R': 44,
    'c': 135000,
    'theta': 137.5,
    'pc': 65,
    'G': 300,
    'e0': 0.035,
    'gamma': 0.015,
}

def calculate_denominator(alpha, beta, theta, c):
    """保留以兼容旧接口"""
    return np.nan  # 不再使用旧闭式解

def calculate_prices_N(alpha, beta, m, w, s, mu_M, mu_R, c, theta, pc, e0, gamma):
    """Compatibility wrapper: 非合作均衡价格 (Prop 1)"""
    return calc_prices_N(alpha, beta, m, w, s, mu_M, mu_R, c, theta, pc, e0, gamma)

def calculate_prices_C(alpha, beta, m, w, s, mu_M, mu_R, c, theta, pc, e0, gamma):
    """Compatibility wrapper: Biform 均衡价格 (Prop 4)"""
    return calc_prices_C(alpha, beta, m, w, s, mu_M, mu_R, c, theta, pc, e0, gamma, G=300)

def calculate_quantities(p_M, p_R, alpha, beta):
    """Calculate quantities q_M and q_R"""
    q_M = alpha * p_M - beta * p_R
    q_R = alpha * p_R - beta * p_M
    return q_M, q_R

def calculate_k_N(p_M, p_R, alpha, beta, theta, pc, gamma, c):
    """Calculate k for non-cooperative case"""
    return calc_k_N(p_M, p_R, alpha, beta, theta, pc, gamma, c)

def calculate_k_C(p_M, p_R, alpha, beta, theta, pc, gamma, c):
    """Calculate k for cooperative case"""
    return calc_k_C(p_M, p_R, alpha, beta, theta, pc, gamma, c)

def calculate_profit_M_N(p_M, p_R, q_M, k, theta, w, s, mu_M):
    """Calculate M's profit for non-cooperative case"""
    Pi_M = (theta * k - p_M - w - mu_M + s) * q_M
    return Pi_M

def calculate_profit_R_N(p_M, p_R, q_M, q_R, k, theta, w, m, s, mu_R, pc, e0, gamma, c, G, alpha, beta):
    """Calculate R's profit for non-cooperative case"""
    Pi_R = (theta * k - p_R - m - mu_R + s) * q_R + (w - m) * q_M \
           + theta**2 * q_R**2 / (2*c) \
           - pc * ((e0 - gamma * k) * (alpha - beta) * (p_M + p_R) - G)
    return Pi_R

def calculate_profit_M_C(p_M, p_R, alpha, beta, theta, s, w, mu_M, c):
    """Shapley 分配 φ_M（正确版，含碳排放项）"""
    return calc_phi_M(p_M, p_R, alpha, beta, theta, s, w, mu_M, c)

def calculate_profit_R_C(p_M, p_R, alpha, beta, theta, s, w, m, mu_R, pc, e0, gamma, c, G):
    """Shapley 分配 φ_R（正确版，含碳排放项）"""
    return calc_phi_R(p_M, p_R, alpha, beta, theta, s, w, m, mu_R, pc, e0, gamma, c, G)

def calculate_n_C(p_M, p_R, alpha, beta):
    """Calculate n for cooperative case"""
    return calc_n_C(p_M, p_R, alpha, beta)

# ==================== FIGURE 1 ====================
def plot_figure1():
    """Figure 1: 3D plots for profit surfaces"""
    fig = plt.figure(figsize=(18, 6))

    params = BASE_PARAMS.copy()

    # (a) alpha and beta vs profits - adjusted range for valid data
    ax1 = fig.add_subplot(131, projection='3d')
    alpha_range = np.linspace(1.35, 1.65, 25)
    beta_range = np.linspace(0.11, 0.15, 25)
    Alpha, Beta = np.meshgrid(alpha_range, beta_range)

    profit_M_bi = np.full_like(Alpha, np.nan)
    profit_M_nc = np.full_like(Alpha, np.nan)
    profit_R_bi = np.full_like(Alpha, np.nan)
    profit_R_nc = np.full_like(Alpha, np.nan)

    for i in range(Alpha.shape[0]):
        for j in range(Alpha.shape[1]):
            a, b = Alpha[i, j], Beta[i, j]
            if a > b + 0.02:
                try:
                    p_M, p_R = calculate_prices_C(a, b, params['m'], params['w'], params['s'],
                                              params['mu_M'], params['mu_R'], params['c'],
                                              params['theta'], params['pc'], params['e0'], params['gamma'])

                    if not (np.isfinite(p_M) and np.isfinite(p_R)):
                        continue

                    profit_M_bi[i, j] = calculate_profit_M_C(p_M, p_R, a, b, params['theta'],
                                                          params['s'], params['w'], params['mu_M'], params['c'])
                    profit_R_bi[i, j] = calculate_profit_R_C(p_M, p_R, a, b, params['theta'],
                                                          params['s'], params['w'], params['m'], params['mu_R'],
                                                          params['pc'], params['e0'], params['gamma'], params['c'], params['G'])

                    p_M_n, p_R_n = calculate_prices_N(a, b, params['m'], params['w'], params['s'],
                                                  params['mu_M'], params['mu_R'], params['c'],
                                                  params['theta'], params['pc'], params['e0'], params['gamma'])

                    if not (np.isfinite(p_M_n) and np.isfinite(p_R_n)):
                        continue

                    q_M_n, q_R_n = calculate_quantities(p_M_n, p_R_n, a, b)
                    k_n = calculate_k_N(p_M_n, p_R_n, a, b, params['theta'], params['pc'], params['gamma'], params['c'])

                    profit_M_nc[i, j] = calculate_profit_M_N(p_M_n, p_R_n, q_M_n, k_n, params['theta'],
                                                            params['w'], params['s'], params['mu_M'])
                    profit_R_nc[i, j] = calculate_profit_R_N(p_M_n, p_R_n, q_M_n, q_R_n, k_n, params['theta'],
                                                            params['w'], params['m'], params['s'], params['mu_R'],
                                                            params['pc'], params['e0'], params['gamma'], params['c'], params['G'],
                                                            a, b)
                except:
                    pass

    # Valid mask - ensure positive values
    valid_mask = (profit_M_bi > 0) & (profit_R_bi > 0) & (profit_M_nc > 0) & (profit_R_nc > 0) & \
                np.isfinite(profit_M_bi) & np.isfinite(profit_R_bi) & np.isfinite(profit_M_nc) & np.isfinite(profit_R_nc)

    ax1.plot_surface(Alpha, Beta, np.where(valid_mask, profit_M_bi/1e6, np.nan),
                   alpha=0.7, color=MORANDI_COLORS['blue'], rstride=1, cstride=1)
    ax1.plot_surface(Alpha, Beta, np.where(valid_mask, profit_R_bi/1e6, np.nan),
                   alpha=0.7, color=MORANDI_COLORS['green'], rstride=1, cstride=1)
    ax1.plot_surface(Alpha, Beta, np.where(valid_mask, profit_M_nc/1e6, np.nan),
                   alpha=0.7, color=MORANDI_COLORS['red'], rstride=1, cstride=1)
    ax1.plot_surface(Alpha, Beta, np.where(valid_mask, profit_R_nc/1e6, np.nan),
                   alpha=0.7, color=MORANDI_COLORS['orange'], rstride=1, cstride=1)

    ax1.set_xlabel(r'$\alpha$')
    ax1.set_ylabel(r'$\beta$')
    ax1.set_zlabel(r'Profit ($\times 10^6$)')
    ax1.view_init(elev=25, azim=45)
    ax1.xaxis.pane.fill = False
    ax1.yaxis.pane.fill = False
    ax1.zaxis.pane.fill = False

    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color=MORANDI_COLORS['blue'], linewidth=2, label='M (Biform)'),
        Line2D([0], [0], color=MORANDI_COLORS['green'], linewidth=2, label='R (Biform)'),
        Line2D([0], [0], color=MORANDI_COLORS['red'], linewidth=2, label='M (Non-coop)'),
        Line2D([0], [0], color=MORANDI_COLORS['orange'], linewidth=2, label='R (Non-coop)'),
    ]
    ax1.legend(handles=legend_elements, loc='upper left', fontsize=9)

    # (b) w and s vs profits
    ax2 = fig.add_subplot(132, projection='3d')
    w_range = np.linspace(30, 40, 25)
    s_range = np.linspace(80, 95, 25)
    W, S = np.meshgrid(w_range, s_range)

    profit_M_bi_ws = np.full_like(W, np.nan)
    profit_M_nc_ws = np.full_like(W, np.nan)
    profit_R_bi_ws = np.full_like(W, np.nan)
    profit_R_nc_ws = np.full_like(W, np.nan)

    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            wi, si = W[i, j], S[i, j]
            if si > wi + params['mu_M']:
                try:
                    p_M, p_R = calculate_prices_C(params['alpha'], params['beta'], params['m'], wi, si,
                                                  params['mu_M'], params['mu_R'], params['c'],
                                                  params['theta'], params['pc'], params['e0'], params['gamma'])

                    if not (np.isfinite(p_M) and np.isfinite(p_R)):
                        continue

                    profit_M_bi_ws[i, j] = calculate_profit_M_C(p_M, p_R, params['alpha'], params['beta'], params['theta'],
                                                           si, wi, params['mu_M'], params['c'])
                    profit_R_bi_ws[i, j] = calculate_profit_R_C(p_M, p_R, params['alpha'], params['beta'], params['theta'],
                                                           si, wi, params['m'], params['mu_R'],
                                                           params['pc'], params['e0'], params['gamma'], params['c'], params['G'])

                    p_M_n, p_R_n = calculate_prices_N(params['alpha'], params['beta'], params['m'], wi, si,
                                                  params['mu_M'], params['mu_R'], params['c'],
                                                  params['theta'], params['pc'], params['e0'], params['gamma'])

                    if not (np.isfinite(p_M_n) and np.isfinite(p_R_n)):
                        continue

                    q_M_n, q_R_n = calculate_quantities(p_M_n, p_R_n, params['alpha'], params['beta'])
                    k_n = calculate_k_N(p_M_n, p_R_n, params['alpha'], params['beta'], params['theta'], params['pc'], params['gamma'], params['c'])

                    profit_M_nc_ws[i, j] = calculate_profit_M_N(p_M_n, p_R_n, q_M_n, k_n, params['theta'],
                                                            wi, si, params['mu_M'])
                    profit_R_nc_ws[i, j] = calculate_profit_R_N(p_M_n, p_R_n, q_M_n, q_R_n, k_n, params['theta'],
                                                            wi, params['m'], si, params['mu_R'],
                                                            params['pc'], params['e0'], params['gamma'], params['c'], params['G'],
                                                            params['alpha'], params['beta'])
                except:
                    pass

    valid_ws = (profit_M_bi_ws > 0) & (profit_R_bi_ws > 0) & (profit_M_nc_ws > 0) & (profit_R_nc_ws > 0) & \
              np.isfinite(profit_M_bi_ws) & np.isfinite(profit_R_bi_ws) & np.isfinite(profit_M_nc_ws) & np.isfinite(profit_R_nc_ws)

    ax2.plot_surface(W, S, np.where(valid_ws, profit_M_bi_ws/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['blue'], rstride=1, cstride=1)
    ax2.plot_surface(W, S, np.where(valid_ws, profit_R_bi_ws/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['green'], rstride=1, cstride=1)
    ax2.plot_surface(W, S, np.where(valid_ws, profit_M_nc_ws/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['red'], rstride=1, cstride=1)
    ax2.plot_surface(W, S, np.where(valid_ws, profit_R_nc_ws/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['orange'], rstride=1, cstride=1)

    ax2.set_xlabel(r'$w$')
    ax2.set_ylabel(r'$s$')
    ax2.set_zlabel(r'Profit ($\times 10^6$)')
    ax2.view_init(elev=25, azim=45)
    ax2.xaxis.pane.fill = False
    ax2.yaxis.pane.fill = False
    ax2.zaxis.pane.fill = False
    ax2.legend(handles=legend_elements, loc='upper left', fontsize=9)

    # (c) theta and mu_R - mu_M vs profits
    ax3 = fig.add_subplot(133, projection='3d')
    theta_range = np.linspace(125, 155, 25)
    mu_diff_range = np.linspace(12, 28, 25)
    Theta, Mu_diff = np.meshgrid(theta_range, mu_diff_range)

    profit_M_bi_tm = np.full_like(Theta, np.nan)
    profit_M_nc_tm = np.full_like(Theta, np.nan)
    profit_R_bi_tm = np.full_like(Theta, np.nan)
    profit_R_nc_tm = np.full_like(Theta, np.nan)

    for i in range(Theta.shape[0]):
        for j in range(Theta.shape[1]):
            th, md = Theta[i, j], Mu_diff[i, j]
            mu_M = params['mu_M']
            mu_R = mu_M + md
            try:
                p_M, p_R = calculate_prices_C(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                          mu_M, mu_R, params['c'], th, params['pc'], params['e0'], params['gamma'])

                if not (np.isfinite(p_M) and np.isfinite(p_R)):
                    continue

                profit_M_bi_tm[i, j] = calculate_profit_M_C(p_M, p_R, params['alpha'], params['beta'], th,
                                                         params['s'], params['w'], mu_M, params['c'])
                profit_R_bi_tm[i, j] = calculate_profit_R_C(p_M, p_R, params['alpha'], params['beta'], th,
                                                         params['s'], params['w'], params['m'], mu_R,
                                                         params['pc'], params['e0'], params['gamma'], params['c'], params['G'])

                p_M_n, p_R_n = calculate_prices_N(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                              mu_M, mu_R, params['c'], th, params['pc'], params['e0'], params['gamma'])

                if not (np.isfinite(p_M_n) and np.isfinite(p_R_n)):
                    continue

                q_M_n, q_R_n = calculate_quantities(p_M_n, p_R_n, params['alpha'], params['beta'])
                k_n = calculate_k_N(p_M_n, p_R_n, params['alpha'], params['beta'], th, params['pc'], params['gamma'], params['c'])

                profit_M_nc_tm[i, j] = calculate_profit_M_N(p_M_n, p_R_n, q_M_n, k_n, th,
                                                       params['w'], params['s'], mu_M)
                profit_R_nc_tm[i, j] = calculate_profit_R_N(p_M_n, p_R_n, q_M_n, q_R_n, k_n, th,
                                                       params['w'], params['m'], params['s'], mu_R,
                                                       params['pc'], params['e0'], params['gamma'], params['c'], params['G'],
                                                       params['alpha'], params['beta'])
            except:
                pass

    valid_tm = (profit_M_bi_tm > 0) & (profit_R_bi_tm > 0) & (profit_M_nc_tm > 0) & (profit_R_nc_tm > 0) & \
              np.isfinite(profit_M_bi_tm) & np.isfinite(profit_R_bi_tm) & np.isfinite(profit_M_nc_tm) & np.isfinite(profit_R_nc_tm)

    ax3.plot_surface(Theta, Mu_diff, np.where(valid_tm, profit_M_bi_tm/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['blue'], rstride=1, cstride=1)
    ax3.plot_surface(Theta, Mu_diff, np.where(valid_tm, profit_R_bi_tm/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['green'], rstride=1, cstride=1)
    ax3.plot_surface(Theta, Mu_diff, np.where(valid_tm, profit_M_nc_tm/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['red'], rstride=1, cstride=1)
    ax3.plot_surface(Theta, Mu_diff, np.where(valid_tm, profit_R_nc_tm/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['orange'], rstride=1, cstride=1)

    ax3.set_xlabel(r'$\theta$')
    ax3.set_ylabel(r'$\mu_R - \mu_M$')
    ax3.set_zlabel(r'Profit ($\times 10^6$)')
    ax3.view_init(elev=25, azim=45)
    ax3.xaxis.pane.fill = False
    ax3.yaxis.pane.fill = False
    ax3.zaxis.pane.fill = False
    ax3.legend(handles=legend_elements, loc='upper left', fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, 'figure1.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(FIGURE_DIR, 'figure1.pdf'), bbox_inches='tight')
    plt.close()
    print("Figure 1 saved.")

# ==================== FIGURE 2 ====================
def plot_figure2():
    """Figure 2: 3D plots for k (collection rate)"""
    fig = plt.figure(figsize=(12, 6))

    params = BASE_PARAMS.copy()

    # (a) theta and gamma vs k
    ax1 = fig.add_subplot(121, projection='3d')
    theta_range = np.linspace(125, 155, 25)
    gamma_range = np.linspace(0.010, 0.020, 25)
    Theta, Gamma = np.meshgrid(theta_range, gamma_range)

    k_bi_tg = np.full_like(Theta, np.nan)
    k_nc_tg = np.full_like(Theta, np.nan)

    for i in range(Theta.shape[0]):
        for j in range(Theta.shape[1]):
            th, ga = Theta[i, j], Gamma[i, j]
            try:
                p_M, p_R = calculate_prices_C(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                              params['mu_M'], params['mu_R'], params['c'], th, params['pc'], params['e0'], ga)
                k_bi_tg[i, j] = calculate_k_C(p_M, p_R, params['alpha'], params['beta'], th, params['pc'], ga, params['c'])

                p_M_n, p_R_n = calculate_prices_N(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                              params['mu_M'], params['mu_R'], params['c'], th, params['pc'], params['e0'], ga)
                k_nc_tg[i, j] = calculate_k_N(p_M_n, p_R_n, params['alpha'], params['beta'], th, params['pc'], ga, params['c'])
            except:
                pass

    valid_tg = (k_bi_tg > 0) & (k_nc_tg > 0) & np.isfinite(k_bi_tg) & np.isfinite(k_nc_tg)

    ax1.plot_surface(Theta, Gamma, np.where(valid_tg, k_bi_tg*100, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['blue'], rstride=1, cstride=1)
    ax1.plot_surface(Theta, Gamma, np.where(valid_tg, k_nc_tg*100, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['red'], rstride=1, cstride=1)

    ax1.set_xlabel(r'$\theta$')
    ax1.set_ylabel(r'$\gamma$')
    ax1.set_zlabel(r'$k$ (%)')
    ax1.view_init(elev=25, azim=45)
    ax1.xaxis.pane.fill = False
    ax1.yaxis.pane.fill = False
    ax1.zaxis.pane.fill = False

    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color=MORANDI_COLORS['blue'], linewidth=2, label='Biform'),
        Line2D([0], [0], color=MORANDI_COLORS['red'], linewidth=2, label='Non-coop'),
    ]
    ax1.legend(handles=legend_elements, loc='upper left', fontsize=9)

    # (b) alpha and beta vs k
    ax2 = fig.add_subplot(122, projection='3d')
    alpha_range = np.linspace(1.35, 1.65, 25)
    beta_range = np.linspace(0.11, 0.15, 25)
    Alpha, Beta = np.meshgrid(alpha_range, beta_range)

    k_bi_ab = np.full_like(Alpha, np.nan)
    k_nc_ab = np.full_like(Alpha, np.nan)

    for i in range(Alpha.shape[0]):
        for j in range(Alpha.shape[1]):
            a, b = Alpha[i, j], Beta[i, j]
            if a > b + 0.02:
                try:
                    p_M, p_R = calculate_prices_C(a, b, params['m'], params['w'], params['s'],
                                                      params['mu_M'], params['mu_R'], params['c'],
                                                      params['theta'], params['pc'], params['e0'], params['gamma'])
                    k_bi_ab[i, j] = calculate_k_C(p_M, p_R, a, b, params['theta'], params['pc'], params['gamma'], params['c'])

                    p_M_n, p_R_n = calculate_prices_N(a, b, params['m'], params['w'], params['s'],
                                                          params['mu_M'], params['mu_R'], params['c'],
                                                          params['theta'], params['pc'], params['e0'], params['gamma'])
                    k_nc_ab[i, j] = calculate_k_N(p_M_n, p_R_n, a, b, params['theta'], params['pc'], params['gamma'], params['c'])
                except:
                    pass

    valid_ab = (k_bi_ab > 0) & (k_nc_ab > 0) & np.isfinite(k_bi_ab) & np.isfinite(k_nc_ab)

    ax2.plot_surface(Alpha, Beta, np.where(valid_ab, k_bi_ab*100, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['blue'], rstride=1, cstride=1)
    ax2.plot_surface(Alpha, Beta, np.where(valid_ab, k_nc_ab*100, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['red'], rstride=1, cstride=1)

    ax2.set_xlabel(r'$\alpha$')
    ax2.set_ylabel(r'$\beta$')
    ax2.set_zlabel(r'$k$ (%)')
    ax2.view_init(elev=25, azim=45)
    ax2.xaxis.pane.fill = False
    ax2.yaxis.pane.fill = False
    ax2.zaxis.pane.fill = False
    ax2.legend(handles=legend_elements, loc='upper left', fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, 'figure2.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(FIGURE_DIR, 'figure2.pdf'), bbox_inches='tight')
    plt.close()
    print("Figure 2 saved.")

# ==================== FIGURE 3 ====================
def plot_figure3():
    """Figure 3: pc and e vs profits (M and R separately)"""
    fig = plt.figure(figsize=(12, 6))

    params = BASE_PARAMS.copy()

    # (a) pc and e vs M profit
    ax1 = fig.add_subplot(121, projection='3d')
    pc_range = np.linspace(50, 80, 25)
    e_range = np.linspace(0.020, 0.050, 25)
    Pc, E = np.meshgrid(pc_range, e_range)

    profit_M_bi_pe = np.full_like(Pc, np.nan)
    profit_M_nc_pe = np.full_like(Pc, np.nan)

    for i in range(Pc.shape[0]):
        for j in range(Pc.shape[1]):
            pc_val, e_val = Pc[i, j], E[i, j]
            try:
                p_M, p_R = calculate_prices_C(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                              params['mu_M'], params['mu_R'], params['c'],
                                              params['theta'], pc_val, e_val, params['gamma'])

                if not (np.isfinite(p_M) and np.isfinite(p_R)):
                    continue

                profit_M_bi_pe[i, j] = calculate_profit_M_C(p_M, p_R, params['alpha'], params['beta'], params['theta'],
                                                          params['s'], params['w'], params['mu_M'], params['c'])

                p_M_n, p_R_n = calculate_prices_N(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                              params['mu_M'], params['mu_R'], params['c'],
                                              params['theta'], pc_val, e_val, params['gamma'])

                if not (np.isfinite(p_M_n) and np.isfinite(p_R_n)):
                    continue

                q_M_n, q_R_n = calculate_quantities(p_M_n, p_R_n, params['alpha'], params['beta'])
                k_n = calculate_k_N(p_M_n, p_R_n, params['alpha'], params['beta'], params['theta'], pc_val, params['gamma'], params['c'])

                profit_M_nc_pe[i, j] = calculate_profit_M_N(p_M_n, p_R_n, q_M_n, k_n, params['theta'],
                                                          params['w'], params['s'], params['mu_M'])
            except:
                pass

    valid_pe = (profit_M_bi_pe > 0) & (profit_M_nc_pe > 0) & np.isfinite(profit_M_bi_pe) & np.isfinite(profit_M_nc_pe)

    ax1.plot_surface(Pc, E, np.where(valid_pe, profit_M_bi_pe/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['blue'], rstride=1, cstride=1)
    ax1.plot_surface(Pc, E, np.where(valid_pe, profit_M_nc_pe/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['red'], rstride=1, cstride=1)

    ax1.set_xlabel(r'$p_c$')
    ax1.set_ylabel(r'$e$')
    ax1.set_zlabel(r'$\Pi_M$ ($\times 10^6$)')
    ax1.view_init(elev=25, azim=45)
    ax1.xaxis.pane.fill = False
    ax1.yaxis.pane.fill = False
    ax1.zaxis.pane.fill = False

    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color=MORANDI_COLORS['blue'], linewidth=2, label='Biform'),
        Line2D([0], [0], color=MORANDI_COLORS['red'], linewidth=2, label='Non-coop'),
    ]
    ax1.legend(handles=legend_elements, loc='upper left', fontsize=9)

    # (b) pc and e vs R profit
    ax2 = fig.add_subplot(122, projection='3d')
    profit_R_bi_pe = np.full_like(Pc, np.nan)
    profit_R_nc_pe = np.full_like(Pc, np.nan)

    for i in range(Pc.shape[0]):
        for j in range(Pc.shape[1]):
            pc_val, e_val = Pc[i, j], E[i, j]
            try:
                p_M, p_R = calculate_prices_C(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                              params['mu_M'], params['mu_R'], params['c'],
                                              params['theta'], pc_val, e_val, params['gamma'])

                if not (np.isfinite(p_M) and np.isfinite(p_R)):
                    continue

                profit_R_bi_pe[i, j] = calculate_profit_R_C(p_M, p_R, params['alpha'], params['beta'], params['theta'],
                                                          params['s'], params['w'], params['m'], params['mu_R'],
                                                          pc_val, e_val, params['gamma'], params['c'], params['G'])

                p_M_n, p_R_n = calculate_prices_N(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                              params['mu_M'], params['mu_R'], params['c'],
                                              params['theta'], pc_val, e_val, params['gamma'])

                if not (np.isfinite(p_M_n) and np.isfinite(p_R_n)):
                    continue

                q_M_n, q_R_n = calculate_quantities(p_M_n, p_R_n, params['alpha'], params['beta'])
                k_n = calculate_k_N(p_M_n, p_R_n, params['alpha'], params['beta'], params['theta'], pc_val, params['gamma'], params['c'])

                profit_R_nc_pe[i, j] = calculate_profit_R_N(p_M_n, p_R_n, q_M_n, q_R_n, k_n, params['theta'],
                                                          params['w'], params['m'], params['s'], params['mu_R'],
                                                          pc_val, e_val, params['gamma'], params['c'], params['G'],
                                                          params['alpha'], params['beta'])
            except:
                pass

    valid_re = (profit_R_bi_pe > 0) & (profit_R_nc_pe > 0) & np.isfinite(profit_R_bi_pe) & np.isfinite(profit_R_nc_pe)

    ax2.plot_surface(Pc, E, np.where(valid_re, profit_R_bi_pe/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['green'], rstride=1, cstride=1)
    ax2.plot_surface(Pc, E, np.where(valid_re, profit_R_nc_pe/1e6, np.nan),
                     alpha=0.7, color=MORANDI_COLORS['orange'], rstride=1, cstride=1)

    ax2.set_xlabel(r'$p_c$')
    ax2.set_ylabel(r'$e$')
    ax2.set_zlabel(r'$\Pi_R$ ($\times 10^6$)')
    ax2.view_init(elev=25, azim=45)
    ax2.xaxis.pane.fill = False
    ax2.yaxis.pane.fill = False
    ax2.zaxis.pane.fill = False
    ax2.legend(handles=legend_elements, loc='upper left', fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, 'figure3.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(FIGURE_DIR, 'figure3.pdf'), bbox_inches='tight')
    plt.close()
    print("Figure 3 saved.")

# ==================== FIGURE 4 ====================
def plot_figure4():
    """Figure 4: 2D plots for pc effects in biform case - with crossover"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    params = BASE_PARAMS.copy()
    # Extended range for crossover
    pc_range = np.linspace(40, 85, 150)

    pM_vals_bi, pR_vals_bi = [], []
    pM_vals_nc, pR_vals_nc = [], []
    qM_vals_bi, qR_vals_bi = [], []
    qM_vals_nc, qR_vals_nc = [], []
    qtotal_bi, qtotal_nc = [], []
    n_vals_bi, k_vals_bi = [], []
    n_vals_nc, k_vals_nc = [], []

    for pc_val in pc_range:
        # Biform
        p_M_bi, p_R_bi = calculate_prices_C(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                    params['mu_M'], params['mu_R'], params['c'],
                                    params['theta'], pc_val, params['e0'], params['gamma'])
        q_M_bi, q_R_bi = calculate_quantities(p_M_bi, p_R_bi, params['alpha'], params['beta'])
        k_bi = calculate_k_C(p_M_bi, p_R_bi, params['alpha'], params['beta'], params['theta'], pc_val, params['gamma'], params['c'])
        n_bi = calculate_n_C(p_M_bi, p_R_bi, params['alpha'], params['beta'])

        # Non-coop
        p_M_nc, p_R_nc = calculate_prices_N(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                    params['mu_M'], params['mu_R'], params['c'],
                                    params['theta'], pc_val, params['e0'], params['gamma'])
        q_M_nc, q_R_nc = calculate_quantities(p_M_nc, p_R_nc, params['alpha'], params['beta'])
        k_nc = calculate_k_N(p_M_nc, p_R_nc, params['alpha'], params['beta'], params['theta'], pc_val, params['gamma'], params['c'])
        n_nc = calculate_n_C(p_M_nc, p_R_nc, params['alpha'], params['beta'])

        if np.isfinite(p_M_bi) and np.isfinite(p_R_bi):
            pM_vals_bi.append(p_M_bi)
            pR_vals_bi.append(p_R_bi)
            qM_vals_bi.append(q_M_bi)
            qR_vals_bi.append(q_R_bi)
            qtotal_bi.append(q_M_bi + q_R_bi)
            n_vals_bi.append(n_bi)
            k_vals_bi.append(k_bi)

        if np.isfinite(p_M_nc) and np.isfinite(p_R_nc):
            pM_vals_nc.append(p_M_nc)
            pR_vals_nc.append(p_R_nc)
            qM_vals_nc.append(q_M_nc)
            qR_vals_nc.append(q_R_nc)
            qtotal_nc.append(q_M_nc + q_R_nc)
            n_vals_nc.append(n_nc)
            k_vals_nc.append(k_nc)

    pM_vals_bi = np.array(pM_vals_bi)
    pR_vals_bi = np.array(pR_vals_bi)
    pM_vals_nc = np.array(pM_vals_nc)
    pR_vals_nc = np.array(pR_vals_nc)

    # Ensure positive values
    pM_vals_bi = np.where(pM_vals_bi > 0, pM_vals_bi, np.nan)
    pR_vals_bi = np.where(pR_vals_bi > 0, pR_vals_bi, np.nan)
    pM_vals_nc = np.where(pM_vals_nc > 0, pM_vals_nc, np.nan)
    pR_vals_nc = np.where(pR_vals_nc > 0, pR_vals_nc, np.nan)

    # Use shorter array for comparison
    min_len = min(len(pM_vals_bi), len(pM_vals_nc))
    pc_range = pc_range[:min_len]

    # (a) pc vs prices
    axes[0].plot(pc_range, pM_vals_bi[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, label=r'$p_M$ (Bi)')
    axes[0].plot(pc_range, pR_vals_bi[:min_len], color=MORANDI_COLORS['green'], linewidth=2, label=r'$p_R$ (Bi)')
    axes[0].plot(pc_range, pM_vals_nc[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, linestyle='--', label=r'$p_M$ (NC)')
    axes[0].plot(pc_range, pR_vals_nc[:min_len], color=MORANDI_COLORS['green'], linewidth=2, linestyle='--', label=r'$p_R$ (NC)')
    axes[0].set_xlabel(r'$p_c$')
    axes[0].set_ylabel('Price')
    axes[0].legend(loc='upper left', fontsize=9)
    axes[0].grid(False)

    qM_vals_bi = np.array(qM_vals_bi)
    qR_vals_bi = np.array(qR_vals_bi)
    qtotal_bi = np.array(qtotal_bi)
    qM_vals_nc = np.array(qM_vals_nc)
    qR_vals_nc = np.array(qR_vals_nc)
    qtotal_nc = np.array(qtotal_nc)

    qM_vals_bi = np.where(qM_vals_bi > 0, qM_vals_bi, np.nan)
    qR_vals_bi = np.where(qR_vals_bi > 0, qR_vals_bi, np.nan)
    qtotal_bi = np.where(qtotal_bi > 0, qtotal_bi, np.nan)
    qM_vals_nc = np.where(qM_vals_nc > 0, qM_vals_nc, np.nan)
    qR_vals_nc = np.where(qR_vals_nc > 0, qR_vals_nc, np.nan)
    qtotal_nc = np.where(qtotal_nc > 0, qtotal_nc, np.nan)

    # (b) pc vs quantities - show crossover
    axes[1].plot(pc_range, qM_vals_bi[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, label=r'$q_M$ (Bi)')
    axes[1].plot(pc_range, qR_vals_bi[:min_len], color=MORANDI_COLORS['green'], linewidth=2, label=r'$q_R$ (Bi)')
    axes[1].plot(pc_range, qM_vals_nc[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, linestyle='--', label=r'$q_M$ (NC)')
    axes[1].plot(pc_range, qR_vals_nc[:min_len], color=MORANDI_COLORS['green'], linewidth=2, linestyle='--', label=r'$q_R$ (NC)')
    axes[1].set_xlabel(r'$p_c$')
    axes[1].set_ylabel('Quantity')
    axes[1].legend(loc='upper left', fontsize=9)
    axes[1].grid(False)

    n_vals_bi = np.array(n_vals_bi)
    k_vals_bi = np.array(k_vals_bi)
    n_vals_nc = np.array(n_vals_nc)
    k_vals_nc = np.array(k_vals_nc)

    n_vals_bi = np.where((n_vals_bi > 0) & np.isfinite(n_vals_bi), n_vals_bi * 100, np.nan)
    k_vals_bi = np.where((k_vals_bi > 0) & np.isfinite(k_vals_bi), k_vals_bi * 100, np.nan)
    n_vals_nc = np.where((n_vals_nc > 0) & np.isfinite(n_vals_nc), n_vals_nc * 100, np.nan)
    k_vals_nc = np.where((k_vals_nc > 0) & np.isfinite(k_vals_nc), k_vals_nc * 100, np.nan)

    # (c) pc vs n and k - show crossover
    axes[2].plot(pc_range, n_vals_bi[:min_len], color=MORANDI_COLORS['purple'], linewidth=2, label=r'$n$ (Bi)')
    axes[2].plot(pc_range, k_vals_bi[:min_len], color=MORANDI_COLORS['orange'], linewidth=2, label=r'$k$ (Bi)')
    axes[2].plot(pc_range, n_vals_nc[:min_len], color=MORANDI_COLORS['purple'], linewidth=2, linestyle='--', label=r'$n$ (NC)')
    axes[2].plot(pc_range, k_vals_nc[:min_len], color=MORANDI_COLORS['orange'], linewidth=2, linestyle='--', label=r'$k$ (NC)')
    axes[2].set_xlabel(r'$p_c$')
    axes[2].set_ylabel('Value (%)')
    axes[2].legend(loc='upper left', fontsize=9)
    axes[2].grid(False)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, 'figure4.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(FIGURE_DIR, 'figure4.pdf'), bbox_inches='tight')
    plt.close()
    print("Figure 4 saved.")

# ==================== FIGURE 5 ====================
def plot_figure5():
    """Figure 5: 2D plots for e effects in biform case - with crossover"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    params = BASE_PARAMS.copy()
    e_range = np.linspace(0.015, 0.055, 150)

    pM_vals_bi, pR_vals_bi = [], []
    pM_vals_nc, pR_vals_nc = [], []
    qM_vals_bi, qR_vals_bi = [], []
    qM_vals_nc, qR_vals_nc = [], []
    qtotal_bi, qtotal_nc = [], []
    n_vals_bi, k_vals_bi = [], []
    n_vals_nc, k_vals_nc = [], []

    for e_val in e_range:
        # Biform
        p_M_bi, p_R_bi = calculate_prices_C(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                    params['mu_M'], params['mu_R'], params['c'],
                                    params['theta'], params['pc'], e_val, params['gamma'])
        q_M_bi, q_R_bi = calculate_quantities(p_M_bi, p_R_bi, params['alpha'], params['beta'])
        k_bi = calculate_k_C(p_M_bi, p_R_bi, params['alpha'], params['beta'], params['theta'], params['pc'], params['gamma'], params['c'])
        n_bi = calculate_n_C(p_M_bi, p_R_bi, params['alpha'], params['beta'])

        # Non-coop
        p_M_nc, p_R_nc = calculate_prices_N(params['alpha'], params['beta'], params['m'], params['w'], params['s'],
                                    params['mu_M'], params['mu_R'], params['c'],
                                    params['theta'], params['pc'], e_val, params['gamma'])
        q_M_nc, q_R_nc = calculate_quantities(p_M_nc, p_R_nc, params['alpha'], params['beta'])
        k_nc = calculate_k_N(p_M_nc, p_R_nc, params['alpha'], params['beta'], params['theta'], params['pc'], params['gamma'], params['c'])
        n_nc = calculate_n_C(p_M_nc, p_R_nc, params['alpha'], params['beta'])

        if np.isfinite(p_M_bi) and np.isfinite(p_R_bi):
            pM_vals_bi.append(p_M_bi)
            pR_vals_bi.append(p_R_bi)
            qM_vals_bi.append(q_M_bi)
            qR_vals_bi.append(q_R_bi)
            qtotal_bi.append(q_M_bi + q_R_bi)
            n_vals_bi.append(n_bi)
            k_vals_bi.append(k_bi)

        if np.isfinite(p_M_nc) and np.isfinite(p_R_nc):
            pM_vals_nc.append(p_M_nc)
            pR_vals_nc.append(p_R_nc)
            qM_vals_nc.append(q_M_nc)
            qR_vals_nc.append(q_R_nc)
            qtotal_nc.append(q_M_nc + q_R_nc)
            n_vals_nc.append(n_nc)
            k_vals_nc.append(k_nc)

    pM_vals_bi = np.array(pM_vals_bi)
    pR_vals_bi = np.array(pR_vals_bi)
    pM_vals_nc = np.array(pM_vals_nc)
    pR_vals_nc = np.array(pR_vals_nc)

    # Ensure positive values
    pM_vals_bi = np.where(pM_vals_bi > 0, pM_vals_bi, np.nan)
    pR_vals_bi = np.where(pR_vals_bi > 0, pR_vals_bi, np.nan)
    pM_vals_nc = np.where(pM_vals_nc > 0, pM_vals_nc, np.nan)
    pR_vals_nc = np.where(pR_vals_nc > 0, pR_vals_nc, np.nan)

    min_len = min(len(pM_vals_bi), len(pM_vals_nc))
    e_plot = e_range[:min_len] * 1000

    # (a) e vs prices
    axes[0].plot(e_plot, pM_vals_bi[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, label=r'$p_M$ (Bi)')
    axes[0].plot(e_plot, pR_vals_bi[:min_len], color=MORANDI_COLORS['green'], linewidth=2, label=r'$p_R$ (Bi)')
    axes[0].plot(e_plot, pM_vals_nc[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, linestyle='--', label=r'$p_M$ (NC)')
    axes[0].plot(e_plot, pR_vals_nc[:min_len], color=MORANDI_COLORS['green'], linewidth=2, linestyle='--', label=r'$p_R$ (NC)')
    axes[0].set_xlabel(r'$e$ ($\times 10^{-3}$)')
    axes[0].set_ylabel('Price')
    axes[0].legend(loc='upper left', fontsize=9)
    axes[0].grid(False)

    qM_vals_bi = np.array(qM_vals_bi)
    qR_vals_bi = np.array(qR_vals_bi)
    qtotal_bi = np.array(qtotal_bi)
    qM_vals_nc = np.array(qM_vals_nc)
    qR_vals_nc = np.array(qR_vals_nc)
    qtotal_nc = np.array(qtotal_nc)

    qM_vals_bi = np.where(qM_vals_bi > 0, qM_vals_bi, np.nan)
    qR_vals_bi = np.where(qR_vals_bi > 0, qR_vals_bi, np.nan)
    qtotal_bi = np.where(qtotal_bi > 0, qtotal_bi, np.nan)
    qM_vals_nc = np.where(qM_vals_nc > 0, qM_vals_nc, np.nan)
    qR_vals_nc = np.where(qR_vals_nc > 0, qR_vals_nc, np.nan)
    qtotal_nc = np.where(qtotal_nc > 0, qtotal_nc, np.nan)

    # (b) e vs quantities
    axes[1].plot(e_plot, qM_vals_bi[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, label=r'$q_M$ (Bi)')
    axes[1].plot(e_plot, qR_vals_bi[:min_len], color=MORANDI_COLORS['green'], linewidth=2, label=r'$q_R$ (Bi)')
    axes[1].plot(e_plot, qM_vals_nc[:min_len], color=MORANDI_COLORS['blue'], linewidth=2, linestyle='--', label=r'$q_M$ (NC)')
    axes[1].plot(e_plot, qR_vals_nc[:min_len], color=MORANDI_COLORS['green'], linewidth=2, linestyle='--', label=r'$q_R$ (NC)')
    axes[1].set_xlabel(r'$e$ ($\times 10^{-3}$)')
    axes[1].set_ylabel('Quantity')
    axes[1].legend(loc='upper left', fontsize=9)
    axes[1].grid(False)

    n_vals_bi = np.array(n_vals_bi)
    k_vals_bi = np.array(k_vals_bi)
    n_vals_nc = np.array(n_vals_nc)
    k_vals_nc = np.array(k_vals_nc)

    n_vals_bi = np.where((n_vals_bi > 0) & np.isfinite(n_vals_bi), n_vals_bi * 100, np.nan)
    k_vals_bi = np.where((k_vals_bi > 0) & np.isfinite(k_vals_bi), k_vals_bi * 100, np.nan)
    n_vals_nc = np.where((n_vals_nc > 0) & np.isfinite(n_vals_nc), n_vals_nc * 100, np.nan)
    k_vals_nc = np.where((k_vals_nc > 0) & np.isfinite(k_vals_nc), k_vals_nc * 100, np.nan)

    # (c) e vs n and k
    axes[2].plot(e_plot, n_vals_bi[:min_len], color=MORANDI_COLORS['purple'], linewidth=2, label=r'$n$ (Bi)')
    axes[2].plot(e_plot, k_vals_bi[:min_len], color=MORANDI_COLORS['orange'], linewidth=2, label=r'$k$ (Bi)')
    axes[2].plot(e_plot, n_vals_nc[:min_len], color=MORANDI_COLORS['purple'], linewidth=2, linestyle='--', label=r'$n$ (NC)')
    axes[2].plot(e_plot, k_vals_nc[:min_len], color=MORANDI_COLORS['orange'], linewidth=2, linestyle='--', label=r'$k$ (NC)')
    axes[2].set_xlabel(r'$e$ ($\times 10^{-3}$)')
    axes[2].set_ylabel('Value (%)')
    axes[2].legend(loc='upper left', fontsize=9)
    axes[2].grid(False)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, 'figure5.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(FIGURE_DIR, 'figure5.pdf'), bbox_inches='tight')
    plt.close()
    print("Figure 5 saved.")

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings('ignore')
    print("Generating figures...")
    plot_figure1()
    plot_figure2()
    plot_figure3()
    plot_figure4()
    plot_figure5()
    print("All figures saved successfully!")