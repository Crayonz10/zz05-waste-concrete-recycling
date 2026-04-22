#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Numerical Simulation for Non-cooperative vs Cooperative (Biform) Game Comparison
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
    'orange': '#D4915E',      # 莫兰迪橙
    'purple': '#8B7B9B',     # 莫兰迪紫
    'red': '#B07070',        # 莫兰迪红
    'teal': '#5A9B9B',      # 莫兰迪青
    'gray': '#7A7A7A',       # 莫兰迪灰
    'cream': '#E8DCC8',     # 莫兰迪奶油色
    'darkblue': '#2C4A6E',  # 深蓝
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

# ============== 1. 数值求解核心函数 ==============
def solve_equilibrium(alpha, beta, theta, c, s, w, m, mu_M, mu_R, p_c, e, G, mode='N'):
    """
    数值求解均衡价格 - 使用论文中的解析公式
    mode='N': 非合作博弈 (baseline)
    mode='C': 合作博弈 (biform game)
    """

    # 计算分母 (Eq. 17 in manuscript)
    denom = (alpha - beta)**3 * (alpha + beta) * theta**4 - \
            4 * c * (alpha - beta) * (3 * alpha**2 - beta**2) * theta**2 + \
            4 * c**2 * (4 * alpha**2 - beta**2)

    # 避免除零
    if abs(denom) < 1e-10:
        denom = 1e-10

    # p_M^* 解析公式 (Eq. 16 in manuscript)
    num_pM = (4 * c**2 * (2 * alpha**2 * (s - w - mu_M) +
                          alpha * beta * (s - m - mu_R) -
                          beta**2 * (w - m)) -
              2 * c * theta**2 * ((alpha - beta) *
                                   (alpha**2 * (s - w - mu_M) -
                                    (alpha**2 - alpha * beta + beta**2) * (w - m)) -
                                   alpha * (alpha**2 - alpha * beta + beta**2) * (mu_M - mu_R)) -
              4 * c * alpha * p_c * e * (alpha - beta) * (alpha**2 - alpha * beta + beta**2))

    p_M = num_pM / denom

    # p_R^* 解析公式 (Eq. 18 in manuscript)
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


def compute_profits(alpha, beta, theta, c, s, w, m, mu_M, mu_R, p_c, e, G, p_M, p_R, mode='N'):
    """
    计算利润
    """
    # 回收量
    q_M = alpha * p_M - beta * p_R
    q_R = alpha * p_R - beta * p_M
    q_total = q_M + q_R

    # 转化率 k
    if mode == 'N':
        k = theta * (alpha * p_R - beta * p_M) / c
    else:  # C模式
        k = theta * (alpha - beta) * (p_M + p_R) / c

    # 碳排放超���配额部分
    emissions_excess = e * (alpha - beta) * (p_M + p_R) - G

    # 制造商利润
    if mode == 'N':
        Pi_M = (theta * k - p_M - w - mu_M + s) * q_M
    else:
        # Biform: Shapley value分配
        Pi_M = (s - p_M - w - mu_M) * q_M + \
               theta**2 * (alpha * p_M - beta * p_R) * \
               ((alpha * p_M - beta * p_R) + 2 * (alpha * p_R - beta * p_M)) / (4 * c)

    # 回收商利润
    if mode == 'N':
        Pi_R = (theta * k - p_R - m - mu_R + s) * q_R + \
               (w - m) * q_M + \
               theta**2 * q_R**2 / (2 * c) - \
               p_c * max(emissions_excess, 0)
    else:
        # Biform: Shapley value分配
        Pi_R = (s - p_R - m - mu_R) * q_R + \
               (w - m) * q_M + \
               theta**2 * ((alpha * p_R - beta * p_M)**2 +
                        (alpha * p_M - beta * p_R + alpha * p_R - beta * p_M)**2) / (4 * c) - \
               p_c * max(emissions_excess, 0)

    return Pi_M, Pi_R, q_M, q_R, k


# ============== 2. 基准参数设置 ==============
BASE_PARAMS = {
    'alpha': 1.5,
    'beta': 0.134,
    'theta': 137.5,
    'c': 135000,
    's': 87.5,
    'w': 35,
    'm': 32,
    'mu_M': 25,
    'mu_R': 44,
    'p_c': 65,
    'e': 0.035,
    'G': 300
}


# ============== 3. 数值分析函数 ==============
def analyze_pc_effect(pc_range, beta_val=0.134):
    """分析碳交易价格对利润的影响"""
    Pi_M_N_list, Pi_R_N_list = [], []
    Pi_M_C_list, Pi_R_C_list = [], []

    params = BASE_PARAMS.copy()
    params['beta'] = beta_val

    for pc in pc_range:
        params['p_c'] = pc

        # 非合作博弈
        p_M_N, p_R_N = solve_equilibrium(**params, mode='N')
        Pi_M_N, Pi_R_N, _, _, _ = compute_profits(p_M=p_M_N, p_R=p_R_N, mode='N', **params)

        # 合作博弈
        p_M_C, p_R_C = solve_equilibrium(**params, mode='C')
        Pi_M_C, Pi_R_C, _, _, _ = compute_profits(p_M=p_M_C, p_R=p_R_C, mode='C', **params)

        Pi_M_N_list.append(Pi_M_N)
        Pi_R_N_list.append(Pi_R_N)
        Pi_M_C_list.append(Pi_M_C)
        Pi_R_C_list.append(Pi_R_C)

    return Pi_M_N_list, Pi_R_N_list, Pi_M_C_list, Pi_R_C_list


def analyze_beta_effect(beta_range, pc_val=65):
    """分析竞争强度对利润的影响"""
    Pi_M_N_list, Pi_R_N_list = [], []
    Pi_M_C_list, Pi_R_C_list = [], []

    params = BASE_PARAMS.copy()
    params['p_c'] = pc_val

    for beta in beta_range:
        params['beta'] = beta

        # 非合作博弈
        p_M_N, p_R_N = solve_equilibrium(**params, mode='N')
        Pi_M_N, Pi_R_N, _, _, _ = compute_profits(p_M=p_M_N, p_R=p_R_N, mode='N', **params)

        # 合作博弈
        p_M_C, p_R_C = solve_equilibrium(**params, mode='C')
        Pi_M_C, Pi_R_C, _, _, _ = compute_profits(p_M=p_M_C, p_R=p_R_C, mode='C', **params)

        Pi_M_N_list.append(Pi_M_N)
        Pi_R_N_list.append(Pi_R_N)
        Pi_M_C_list.append(Pi_M_C)
        Pi_R_C_list.append(Pi_R_C)

    return Pi_M_N_list, Pi_R_N_list, Pi_M_C_list, Pi_R_C_list


def analyze_c_effect(c_range, pc_val=65, beta_val=0.134):
    """分析成本系数对利润的影响"""
    Pi_M_N_list, Pi_R_N_list = [], []
    Pi_M_C_list, Pi_R_C_list = [], []

    params = BASE_PARAMS.copy()
    params['p_c'] = pc_val
    params['beta'] = beta_val

    for c in c_range:
        params['c'] = c

        # 非合作博弈
        p_M_N, p_R_N = solve_equilibrium(**params, mode='N')
        Pi_M_N, Pi_R_N, _, _, _ = compute_profits(p_M=p_M_N, p_R=p_R_N, mode='N', **params)

        # 合作博弈
        p_M_C, p_R_C = solve_equilibrium(**params, mode='C')
        Pi_M_C, Pi_R_C, _, _, _ = compute_profits(p_M=p_M_C, p_R=p_R_C, mode='C', **params)

        Pi_M_N_list.append(Pi_M_N)
        Pi_R_N_list.append(Pi_R_N)
        Pi_M_C_list.append(Pi_M_C)
        Pi_R_C_list.append(Pi_R_C)

    return Pi_M_N_list, Pi_R_N_list, Pi_M_C_list, Pi_R_C_list


# ============== 4. 绘图函数 ==============
def plot_profits_vs_param(x_data, y_data_N, y_data_C, param_name, param_unit,
                         save_path, title_suffix=''):
    """
    绘制利润随参数变化的对比图
    使用Morandi配色和Nature风格
    """
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)

    # 设置线条样式 - Morandi配色
    line_width = 2.5
    marker_size = 6

    # 制造商 - 非合作
    ax.plot(x_data, [v/1e6 for v in y_data_N[0]],
            color=MORANDI_COLORS['blue'], linewidth=line_width,
            marker='o', markersize=marker_size, markevery=3,
            label=r'Manufacturer (Non-coop)', linestyle='-')

    # 制造商 - 合作
    ax.plot(x_data, [v/1e6 for v in y_data_C[0]],
            color=MORANDI_COLORS['red'], linewidth=line_width,
            marker='s', markersize=marker_size, markevery=3,
            label=r'Manufacturer (Biform)', linestyle='-')

    # 回收商 - 非合作
    ax.plot(x_data, [v/1e6 for v in y_data_N[1]],
            color=MORANDI_COLORS['green'], linewidth=line_width,
            marker='^', markersize=marker_size, markevery=3,
            label=r'Recycler (Non-coop)', linestyle='--')

    # 回收商 - 合作
    ax.plot(x_data, [v/1e6 for v in y_data_C[1]],
            color=MORANDI_COLORS['orange'], linewidth=line_width,
            marker='d', markersize=marker_size, markevery=3,
            label=r'Recycler (Biform)', linestyle='--')

    # 设置标签和标题
    if param_unit:
        ax.set_xlabel(f'{param_name} ({param_unit})', fontsize=12, fontweight='bold')
    else:
        ax.set_xlabel(f'{param_name}', fontsize=12, fontweight='bold')
    ax.set_ylabel(r'Profit ($\times 10^6$ yuan)', fontsize=12, fontweight='bold')
    ax.set_title(f'Profit Comparison: Non-cooperative vs Biform Game\n{title_suffix}',
               fontsize=13, fontweight='bold', pad=15)

    # 设置图例 - Nature风格
    ax.legend(loc='best', frameon=True, fancybox=True, shadow=True,
             framealpha=0.95, edgecolor=MORANDI_COLORS['gray'])

    # 设置网格 - 优雅样式
    ax.grid(True, linestyle='--', alpha=0.3, color=MORANDI_COLORS['gray'])
    ax.tick_params(axis='both', which='major', direction='in', length=6)

    # 设置边框样式
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_color(MORANDI_COLORS['gray'])

    # 调整布局
    plt.tight_layout()

    # 保存图片 (同时保存png和pdf)
    save_path_png = save_path.replace('.pdf', '.png')
    plt.savefig(save_path, format='pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig(save_path_png, format='png', bbox_inches='tight',
                facecolor='white', edgecolor='none', dpi=300)

    print(f"Figure saved: {save_path}")
    plt.close()


# ============== 5. 主程序 ==============
def main():
    """主程序：生成所有数值分析图"""
    # 创建输出目录
    output_dir = '/Users/zz/Library/CloudStorage/Dropbox/何门撸铁/_gym paper/zz05_合作非合作博弈/zz05_latexfile/simulation/figures'
    os.makedirs(output_dir, exist_ok=True)

    # (1) 碳排放交易价格pc对利润的影响
    print("="*60)
    print("Generating Figure 1: Profit vs Carbon Price (pc)")
    print("="*60)

    pc_range = np.linspace(40, 120, 25)
    Pi_data_pc = analyze_pc_effect(pc_range)

    plot_profits_vs_param(
        pc_range, (Pi_data_pc[0], Pi_data_pc[1]), (Pi_data_pc[2], Pi_data_pc[3]),
        param_name=r'$p_c$', param_unit='yuan/ton',
        save_path=os.path.join(output_dir, 'fig1_profit_vs_pc.pdf'),
        title_suffix=r'Varying Carbon Trading Price $p_c$'
    )

    # (2) 竞争强度beta对利润的影响
    print("\n" + "="*60)
    print("Generating Figure 2: Profit vs Competition Intensity (beta)")
    print("="*60)

    beta_range = np.linspace(0.05, 0.25, 25)
    Pi_data_beta = analyze_beta_effect(beta_range)

    plot_profits_vs_param(
        beta_range, (Pi_data_beta[0], Pi_data_beta[1]), (Pi_data_beta[2], Pi_data_beta[3]),
        param_name=r'$\beta$', param_unit='',
        save_path=os.path.join(output_dir, 'fig2_profit_vs_beta.pdf'),
        title_suffix=r'Varying Competition Intensity $\beta$'
    )

    # (3) 成本系数c对利润的影响
    print("\n" + "="*60)
    print("Generating Figure 3: Profit vs Cost Coefficient (c)")
    print("="*60)

    c_range = np.linspace(80000, 200000, 25)
    Pi_data_c = analyze_c_effect(c_range)

    plot_profits_vs_param(
        c_range, (Pi_data_c[0], Pi_data_c[1]), (Pi_data_c[2], Pi_data_c[3]),
        param_name=r'$\ln(c)$', param_unit='',
        save_path=os.path.join(output_dir, 'fig3_profit_vs_c.pdf'),
        title_suffix=r'Varying Cost Coefficient $\ln(c)$'
    )

    print("\n" + "="*60)
    print("All figures generated successfully!")
    print("="*60)


if __name__ == "__main__":
    main()