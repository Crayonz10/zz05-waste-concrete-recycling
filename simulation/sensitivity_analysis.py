#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Numerical Simulation for Parameter Sensitivity Analysis
Using Morandi colors following Nature/顶刊 aesthetic
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os

# 设置中文字体和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Morandi配色方案 - Nature/顶刊风格
MORANDI_COLORS = {
    'blue': '#4A7C9B',       # 莫兰迪蓝
    'green': '#7A9E7E',      # 莫兰迪绿
    'orange': '#D4915E',     # 莫兰迪橙
    'purple': '#8B7B9B',     # 莫兰迪紫
    'red': '#B07070',        # 莫兰迪红
    'teal': '#5A9B9B',       # 莫兰迪青
    'gray': '#7A7A7A',       # 莫兰迪灰
    'cream': '#E8DCC8',      # 莫兰迪奶油色
    'darkblue': '#2C4A6E',   # 深蓝
    'darkgreen': '#3A5A4E'   # 深绿
}

# 设置绘图样式
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.figsize'] = (8, 6)


# ============== 1. 均衡求解函数 ==============
def solve_equilibrium(alpha, beta, theta, c, s, w, m, mu_M, mu_R, p_c, e, G):
    """数值求解均衡价格 - 使用论文中的解析公式"""

    # 计算分母 (Eq. 17 in manuscript)
    denom = (alpha - beta)**3 * (alpha + beta) * theta**4 - \
            4 * c * (alpha - beta) * (3 * alpha**2 - beta**2) * theta**2 + \
            4 * c**2 * (4 * alpha**2 - beta**2)

    # 避免除零
    if abs(denom) < 1e-10:
        denom = 1e-10

    # p_M^* 解析公式
    num_pM = (4 * c**2 * (2 * alpha**2 * (s - w - mu_M) +
                          alpha * beta * (s - m - mu_R) -
                          beta**2 * (w - m)) -
              2 * c * theta**2 * ((alpha - beta) *
                                   (alpha**2 * (s - w - mu_M) -
                                    (alpha**2 - alpha * beta + beta**2) * (w - m)) -
                                   alpha * (alpha**2 - alpha * beta + beta**2) * (mu_M - mu_R)) -
              4 * c * alpha * p_c * e * (alpha - beta) * (alpha**2 - alpha * beta + beta**2))

    p_M = num_pM / denom

    # p_R^* 解析公式
    num_pR = (4 * c**2 * alpha * (2 * alpha * (s - m - mu_R) +
                                   beta * (s - 3*w + 2*m - mu_M)) -
              2 * c * alpha * theta**2 * ((alpha - beta) *
                                            (alpha * (w - m) +
                                             beta * (s - 3*w + 2*m - mu_M)) +
                                            alpha * (alpha - 2*beta) * (mu_M - mu_R)) -
              4 * c * p_c * e * (alpha - beta) *
              (c * (2*alpha**2 - beta**2) - theta**2 * alpha * (alpha - beta)))

    p_R = num_pR / denom

    return p_M, p_R


def compute_equilibrium(alpha, beta, theta, c, s, w, m, mu_M, mu_R, p_c, e, G):
    """计算完整的均衡结果"""

    p_M, p_R = solve_equilibrium(alpha, beta, theta, c, s, w, m, mu_M, mu_R, p_c, e, G)

    # 回收量
    q_M = alpha * p_M - beta * p_R
    q_R = alpha * p_R - beta * p_M
    q_total = q_M + q_R

    # 转化率 k (non-cooperative)
    k = theta * (alpha * p_R - beta * p_M) / c

    # 碳排放超过配额部分
    emissions_excess = e * (alpha - beta) * (p_M + p_R) - G

    # 制造商利润 (non-cooperative)
    Pi_M = (theta * k - p_M - w - mu_M + s) * q_M

    # 回收商利润 (non-cooperative)
    Pi_R = (theta * k - p_R - m - mu_R + s) * q_R + \
           (w - m) * q_M + \
           theta**2 * q_R**2 / (2 * c) - \
           p_c * max(emissions_excess, 0)

    # 计算 n* (cost-sharing ratio for biform)
    # n* = [2(αp_R - βp_M)² + 2(αp_M - βp_R)(αp_R - βp_M) - (αp_M - βp_R)²] / [2(α-β)²(p_M + p_R)²]
    if (alpha - beta) * (p_M + p_R) > 0:
        n = (2 * (alpha * p_R - beta * p_M)**2 +
             2 * (alpha * p_M - beta * p_R) * (alpha * p_R - beta * p_M) -
             (alpha * p_M - beta * p_R)**2) / \
            (2 * (alpha - beta)**2 * (p_M + p_R)**2)
    else:
        n = 0.5

    # k for biform
    k_C = theta * (alpha - beta) * (p_M + p_R) / c

    # Shapley value profits for biform
    Pi_M_C = (s - p_M - w - mu_M) * q_M + \
             theta**2 * (alpha * p_M - beta * p_R) * \
             ((alpha * p_M - beta * p_R) + 2 * (alpha * p_R - beta * p_M)) / (4 * c)

    Pi_R_C = (s - p_R - m - mu_R) * q_R + \
             (w - m) * q_M + \
             theta**2 * ((alpha * p_R - beta * p_M)**2 +
                      (alpha * p_M - beta * p_R + alpha * p_R - beta * p_M)**2) / (4 * c) - \
             p_c * max(emissions_excess, 0)

    return {
        'p_M': p_M, 'p_R': p_R,
        'q_M': q_M, 'q_R': q_R, 'q_total': q_total,
        'k': k, 'k_C': k_C,
        'n': n,
        'Pi_M': Pi_M, 'Pi_R': Pi_R,
        'Pi_M_C': Pi_M_C, 'Pi_R_C': Pi_R_C
    }


# ============== 2. 基准参数设置 ==============
BASE_PARAMS = {
    'alpha': 1.5,
    'beta': 0.134,
    'theta': 137.5,
    'c': 135000,
    's': 87.5,
    'w': 50,
    'm': 32,
    'mu_M': 25,
    'mu_R': 44,
    'p_c': 65,
    'e': 0.035,
    'G': 300
}


# ============== 3. 参数分析函数 ==============
def analyze_alpha(alpha_range, params):
    """分析价格敏感系数α的影响"""
    results = {
        'p_M': [], 'p_R': [], 'q_M': [], 'q_R': [], 'q_total': [],
        'k': [], 'n': [], 'Pi_M': [], 'Pi_R': []
    }

    for alpha in alpha_range:
        p = params.copy()
        p['alpha'] = alpha
        eq = compute_equilibrium(**p)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['k'].append(eq['k'])
        results['n'].append(eq['n'])
        results['Pi_M'].append(eq['Pi_M'])
        results['Pi_R'].append(eq['Pi_R'])

    return results


def analyze_beta(beta_range, params):
    """分析竞争强度β的影响"""
    results = {
        'p_M': [], 'p_R': [], 'q_M': [], 'q_R': [], 'q_total': [],
        'k': [], 'n': [], 'Pi_M': [], 'Pi_R': []
    }

    for beta in beta_range:
        p = params.copy()
        p['beta'] = beta
        eq = compute_equilibrium(**p)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['k'].append(eq['k'])
        results['n'].append(eq['n'])
        results['Pi_M'].append(eq['Pi_M'])
        results['Pi_R'].append(eq['Pi_R'])

    return results


def analyze_s(s_range, params):
    """分析政府补贴s的影响"""
    results = {
        'p_M': [], 'p_R': [], 'q_M': [], 'q_R': [], 'q_total': [],
        'k': [], 'n': [], 'Pi_M': [], 'Pi_R': []
    }

    for s in s_range:
        p = params.copy()
        p['s'] = s
        eq = compute_equilibrium(**p)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['k'].append(eq['k'])
        results['n'].append(eq['n'])
        results['Pi_M'].append(eq['Pi_M'])
        results['Pi_R'].append(eq['Pi_R'])

    return results


def analyze_theta(theta_range, params):
    """分析潜在回收价值θ的影响"""
    results = {
        'p_M': [], 'p_R': [], 'q_M': [], 'q_R': [], 'q_total': [],
        'k': [], 'n': [], 'Pi_M': [], 'Pi_R': []
    }

    for theta in theta_range:
        p = params.copy()
        p['theta'] = theta
        eq = compute_equilibrium(**p)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['k'].append(eq['k'])
        results['n'].append(eq['n'])
        results['Pi_M'].append(eq['Pi_M'])
        results['Pi_R'].append(eq['Pi_R'])

    return results


def analyze_m(m_range, params):
    """分析运营成本m的影响"""
    results = {
        'p_M': [], 'p_R': [], 'q_M': [], 'q_R': [], 'q_total': [],
        'k': [], 'n': [], 'Pi_M': [], 'Pi_R': []
    }

    for m in m_range:
        p = params.copy()
        p['m'] = m
        eq = compute_equilibrium(**p)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['k'].append(eq['k'])
        results['n'].append(eq['n'])
        results['Pi_M'].append(eq['Pi_M'])
        results['Pi_R'].append(eq['Pi_R'])

    return results


def analyze_w(w_range, params):
    """分析转移价格w的影响"""
    results = {
        'p_M': [], 'p_R': [], 'q_M': [], 'q_R': [], 'q_total': [],
        'k': [], 'n': [], 'Pi_M': [], 'Pi_R': []
    }

    for w in w_range:
        p = params.copy()
        p['w'] = w
        eq = compute_equilibrium(**p)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['k'].append(eq['k'])
        results['n'].append(eq['n'])
        results['Pi_M'].append(eq['Pi_M'])
        results['Pi_R'].append(eq['Pi_R'])

    return results


def analyze_mu_diff(mu_diff_range, params):
    """分析运输成本差值(μ_R - μ_M)的影响，差值大于0表示回收商运输成本更高"""

    # mu_R - mu_M > 0 意味着回收商的运输成本更高
    # 设定基准: mu_M = 25, 取不同的差值
    base_mu_M = 25

    results = {
        'p_M': [], 'p_R': [], 'q_M': [], 'q_R': [], 'q_total': [],
        'k': [], 'n': [], 'Pi_M': [], 'Pi_R': []
    }

    for mu_diff in mu_diff_range:
        p = params.copy()
        p['mu_M'] = base_mu_M
        p['mu_R'] = base_mu_M + mu_diff  # mu_R = mu_M + (mu_R - mu_M)
        eq = compute_equilibrium(**p)
        results['p_M'].append(eq['p_M'])
        results['p_R'].append(eq['p_R'])
        results['q_M'].append(eq['q_M'])
        results['q_R'].append(eq['q_R'])
        results['q_total'].append(eq['q_total'])
        results['k'].append(eq['k'])
        results['n'].append(eq['n'])
        results['Pi_M'].append(eq['Pi_M'])
        results['Pi_R'].append(eq['Pi_R'])

    return results


# ============== 4. 绘图函数 ==============
def plot_4subfigs(x_data, y_data_dict, xlabel, save_path, title_prefix):
    """绘制4子图 (a) 价格 (b) 数量 (c) k和n (d) 利润"""

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # (a) Collection Prices
    ax = axes[0, 0]
    ax.plot(x_data, y_data_dict['p_M'], color=MORANDI_COLORS['blue'], linewidth=2, marker='o', markersize=4, markevery=3, label=r'$p_M^*$')
    ax.plot(x_data, y_data_dict['p_R'], color=MORANDI_COLORS['orange'], linewidth=2, marker='s', markersize=4, markevery=3, label=r'$p_R^*$')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(r'Collection price', fontsize=11)
    ax.legend(loc='best', frameon=True)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_title('(a) Collection Prices', fontweight='bold')

    # (b) Collection Quantities
    ax = axes[0, 1]
    ax.plot(x_data, y_data_dict['q_M'], color=MORANDI_COLORS['blue'], linewidth=2, marker='o', markersize=4, markevery=3, label=r'$q_M^*$')
    ax.plot(x_data, y_data_dict['q_R'], color=MORANDI_COLORS['orange'], linewidth=2, marker='s', markersize=4, markevery=3, label=r'$q_R^*$')
    ax.plot(x_data, y_data_dict['q_total'], color=MORANDI_COLORS['green'], linewidth=2, marker='^', markersize=4, markevery=3, label=r'$Q^*$')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(r'Collection quantity', fontsize=11)
    ax.legend(loc='best', frameon=True)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_title('(b) Collection Quantities', fontweight='bold')

    # (c) k and n
    ax = axes[1, 0]
    ax.plot(x_data, y_data_dict['k'], color=MORANDI_COLORS['purple'], linewidth=2, marker='o', markersize=4, markevery=3, label=r'$k^*$')
    ax.plot(x_data, y_data_dict['n'], color=MORANDI_COLORS['teal'], linewidth=2, marker='s', markersize=4, markevery=3, label=r'$n^*$')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(r'Value', fontsize=11)
    ax.legend(loc='best', frameon=True)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_title('(c) Conversion Rate and Cost-sharing Ratio', fontweight='bold')

    # (d) Profits
    ax = axes[1, 1]
    ax.plot(x_data, y_data_dict['Pi_M'], color=MORANDI_COLORS['blue'], linewidth=2, marker='o', markersize=4, markevery=3, label=r'$\Pi_M^*$')
    ax.plot(x_data, y_data_dict['Pi_R'], color=MORANDI_COLORS['orange'], linewidth=2, marker='s', markersize=4, markevery=3, label=r'$\Pi_R^*$')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(r'Profit', fontsize=11)
    ax.legend(loc='best', frameon=True)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_title('(d) Profits', fontweight='bold')

    plt.tight_layout()

    # 保存
    save_path_pdf = save_path.replace('.png', '.pdf')
    plt.savefig(save_path_pdf, format='pdf', bbox_inches='tight', facecolor='white')
    plt.savefig(save_path, format='png', bbox_inches='tight', facecolor='white', dpi=300)
    plt.close()

    print(f"Figure saved: {save_path}")


def plot_2subfigs(x_data, y_data_dict, xlabel, save_path, title_prefix):
    """绘制2子图 (a) 价格/数量 (b) 利润"""

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # (a) Prices and Quantities
    ax = axes[0]
    ax.plot(x_data, y_data_dict['p_M'], color=MORANDI_COLORS['blue'], linewidth=2, marker='o', markersize=4, markevery=3, label=r'$p_M^*$')
    ax.plot(x_data, y_data_dict['p_R'], color=MORANDI_COLORS['orange'], linewidth=2, marker='s', markersize=4, markevery=3, label=r'$p_R^*$')
    ax.plot(x_data, y_data_dict['q_M'], color=MORANDI_COLORS['green'], linewidth=2, marker='^', markersize=4, markevery=3, label=r'$q_M^*$')
    ax.plot(x_data, y_data_dict['q_R'], color=MORANDI_COLORS['red'], linewidth=2, marker='d', markersize=4, markevery=3, label=r'$q_R^*$')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(r'Value', fontsize=11)
    ax.legend(loc='best', frameon=True)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_title('(a) Prices and Quantities', fontweight='bold')

    # (b) Profits
    ax = axes[1]
    ax.plot(x_data, y_data_dict['Pi_M'], color=MORANDI_COLORS['blue'], linewidth=2, marker='o', markersize=4, markevery=3, label=r'$\Pi_M^*$')
    ax.plot(x_data, y_data_dict['Pi_R'], color=MORANDI_COLORS['orange'], linewidth=2, marker='s', markersize=4, markevery=3, label=r'$\Pi_R^*$')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(r'Profit', fontsize=11)
    ax.legend(loc='best', frameon=True)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_title('(b) Profits', fontweight='bold')

    plt.tight_layout()

    # 保存
    save_path_pdf = save_path.replace('.png', '.pdf')
    plt.savefig(save_path_pdf, format='pdf', bbox_inches='tight', facecolor='white')
    plt.savefig(save_path, format='png', bbox_inches='tight', facecolor='white', dpi=300)
    plt.close()

    print(f"Figure saved: {save_path}")


# ============== 5. 主程序 ==============
def main():
    """主程序：生成所有参数敏感性分析图"""

    output_dir = '/Users/zz/Library/CloudStorage/Dropbox/何门撸铁/_gym paper/zz05_合作非合作博弈/zz05_latexfile/simulation/figures'
    os.makedirs(output_dir, exist_ok=True)

    params = BASE_PARAMS.copy()

    # Fig 1: Impact of α
    print("="*60)
    print("Generating Figure 1: Impact of α (price sensitivity)")
    print("="*60)
    alpha_range = np.linspace(0.889, 3.0, 25)
    results_alpha = analyze_alpha(alpha_range, params)
    plot_4subfigs(alpha_range, results_alpha, r'$\alpha$',
                  os.path.join(output_dir, 'fig_alpha.png'), 'α')

    # Fig 2: Impact of β
    print("\n" + "="*60)
    print("Generating Figure 2: Impact of β (competition intensity)")
    print("="*60)
    beta_range = np.linspace(0.05, 0.25, 25)
    results_beta = analyze_beta(beta_range, params)
    plot_4subfigs(beta_range, results_beta, r'$\beta$',
                  os.path.join(output_dir, 'fig_beta.png'), 'β')

    # Fig 3: Impact of s (ensure positive quantities)
    print("\n" + "="*60)
    print("Generating Figure 3: Impact of s (government subsidy)")
    print("="*60)
    s_range = np.linspace(85, 150, 25)  # Start from 85 to ensure positive q_R and k
    results_s = analyze_s(s_range, params)
    plot_4subfigs(s_range, results_s, r'$s$',
                  os.path.join(output_dir, 'fig_s.png'), 's')

    # Fig 4: Impact of θ
    print("\n" + "="*60)
    print("Generating Figure 4: Impact of θ (potential recycled value)")
    print("="*60)
    theta_range = np.linspace(50, 250, 25)
    results_theta = analyze_theta(theta_range, params)
    plot_4subfigs(theta_range, results_theta, r'$\theta$',
                  os.path.join(output_dir, 'fig_theta.png'), 'θ')

    # Fig 5: Impact of m (ensure positive profits)
    print("\n" + "="*60)
    print("Generating Figure 5: Impact of m (operational cost)")
    print("="*60)
    m_range = np.linspace(15, 34, 25)  # Limit to 34 to ensure positive Pi_R (w=35 > m)
    results_m = analyze_m(m_range, params)
    plot_2subfigs(m_range, results_m, r'$m$',
                  os.path.join(output_dir, 'fig_m.png'), 'm')

    # Fig 6: Impact of w (ensure positive profits)
    print("\n" + "="*60)
    print("Generating Figure 6: Impact of w (outsourcing fee)")
    print("="*60)
    w_range = np.linspace(50, 60, 25)  # Start from 50 to ensure positive n and Pi_R
    results_w = analyze_w(w_range, params)
    plot_2subfigs(w_range, results_w, r'$w$',
                  os.path.join(output_dir, 'fig_w.png'), 'w')

    # Fig 7: Impact of μ_R - μ_M (ensure positive values)
    print("\n" + "="*60)
    print("Generating Figure 7: Impact of μ_R - μ_M (transport cost differential)")
    print("="*60)
    mu_diff_range = np.linspace(5, 17.5, 25)  # Limit to 17.5 to ensure positive n
    results_mu_diff = analyze_mu_diff(mu_diff_range, params)
    plot_4subfigs(mu_diff_range, results_mu_diff, r'$\mu_R - \mu_M$',
                  os.path.join(output_dir, 'fig_mu_diff.png'), 'μ_R-μ_M')

    print("\n" + "="*60)
    print("All Parameter Sensitivity Analysis figures generated successfully!")
    print("="*60)


if __name__ == "__main__":
    main()