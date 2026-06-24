#!/usr/bin/env python3
"""G -> Multiple effects (profit, price, quantity)"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'figure.dpi': 150,
    'savefig.dpi': 300,
})

ALPHA = 1.5
BETA = 0.134
M = 32
W = 35
S = 87.5
MIU_M = 25
MIU_R = 44
C = 135000
THETA = 137.5
PC_VAL = 65
E_VAL = 0.035


def calc_non_coop(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    den = (a-b)**3*(a+b)*th**4 - 4*c*(a-b)*(3*a*a-b*b)*th*th + 4*c*c*(4*a*a-b*b)
    if abs(den) < 1e-10: den = 1e-10
    num_pM = 4*c*c*(2*a*a*(s-w-mM)+a*b*(s-m-mR)-b*b*(w-m)) - 2*c*th*th*((a-b)*(a*a*(s-w-mM)-(a*a-a*b+b*b)*(w-m))-a*(a*a-a*b+b*b)*(mM-mR)) - 4*c*a*pc*e*(a-b)*(a*a-a*b+b*b)
    pM = num_pM / den
    num_pR = 4*c*c*a*(2*a*(s-m-mR)+b*(s-3*w+2*m-mM)) - 2*c*a*th*th*((a-b)*(a*(w-m)+b*(s-3*w+2*m-mM))+a*(a-2*b)*(mM-mR)) - 4*c*pc*e*(a-b)*(c*(2*a*a-b*b)-th*th*a*(a-b))
    pR = num_pR / den
    k_N = th*(a*pR - b*pM) / c
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    q_total = qM + qR
    em = max(e*q_total - G, 0)  # carbon emissions exceeding quota
    Pi_MN = (th*k_N - pM - w - mM + s)*qM
    Pi_RN = (th*k_N - pR - m - mR + s)*qR + (w-m)*qM + th*th*qR*qR/(2*c) - pc*em
    return {'pM': pM, 'pR': pR, 'qM': qM, 'qR': qR, 'q_total': q_total, 'Pi_MN': Pi_MN, 'Pi_RN': Pi_RN, 'Pi_total': Pi_MN + Pi_RN}


def calc_biform(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    den = (a-b)**3*(a+b)*th**4 - 4*c*(a-b)*(3*a*a-b*b)*th*th + 4*c*c*(4*a*a-b*b)
    if abs(den) < 1e-10: den = 1e-10
    num_pM = 4*c*c*(2*a*a*(s-w-mM)+a*b*(s-m-mR)-b*b*(w-m)) - 2*c*th*th*((a-b)*(a*a*(s-w-mM)-(a*a-a*b+b*b)*(w-m))-a*(a*a-a*b+b*b)*(mM-mR)) - 4*c*a*pc*e*(a-b)*(a*a-a*b+b*b)
    pM = num_pM / den
    num_pR = 4*c*c*a*(2*a*(s-m-mR)+b*(s-3*w+2*m-mM)) - 2*c*a*th*th*((a-b)*(a*(w-m)+b*(s-3*w+2*m-mM))+a*(a-2*b)*(mM-mR)) - 4*c*pc*e*(a-b)*(c*(2*a*a-b*b)-th*th*a*(a-b))
    pR = num_pR / den
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    q_total = qM + qR
    em = max(e*q_total - G, 0)
    phi_M = (s - pM - w - mM)*qM + th*th*qM*(qM+2*qR)/(4*c)
    phi_R = (s - pR - m - mR)*qR + (w-m)*qM + th*th*(qR**2+(qM+qR)**2)/(4*c) - pc*em
    return {'pM': pM, 'pR': pR, 'qM': qM, 'qR': qR, 'q_total': q_total, 'phi_M': phi_M, 'phi_R': phi_R, 'phi_total': phi_M + phi_R}


if __name__ == '__main__':
    a, b, th, c, s, w, m, mM, mR = ALPHA, BETA, THETA, C, S, W, M, MIU_M, MIU_R
    pc, e = PC_VAL, E_VAL

    G_vals = np.linspace(100, 500, 50)

    # Non-cooperative results
    pi_mn, pi_rn, pi_total_n = [], [], []
    pR_n = []
    for G_val in G_vals:
        r = calc_non_coop(a, b, th, c, s, w, m, mM, mR, pc, e, G_val)
        pi_mn.append(r['Pi_MN'])
        pi_rn.append(r['Pi_RN'])
        pi_total_n.append(r['Pi_total'])
        pR_n.append(r['pR'])

    # Biform results
    phi_m, phi_r, phi_total = [], [], []
    pR_c = []
    for G_val in G_vals:
        r = calc_biform(a, b, th, c, s, w, m, mM, mR, pc, e, G_val)
        phi_m.append(r['phi_M'])
        phi_r.append(r['phi_R'])
        phi_total.append(r['phi_total'])
        pR_c.append(r['pR'])

    # Create 2x2 subplot
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Plot 1: Recycler profit
    ax1 = axes[0, 0]
    ax1.plot(G_vals, pi_rn, color='#FF6F00', linewidth=2, label='Non-cooperative')
    ax1.plot(G_vals, phi_r, color='#00838F', linewidth=2, label='Biform')
    ax1.set_xlabel(r'$G$', fontsize=12)
    ax1.set_ylabel('Recycler Profit', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_title('(a) Recycler Profit', fontsize=12, fontweight='bold')

    # Plot 2: Manufacturer profit
    ax2 = axes[0, 1]
    ax2.plot(G_vals, pi_mn, color='#FF6F00', linewidth=2, label='Non-cooperative')
    ax2.plot(G_vals, phi_m, color='#00838F', linewidth=2, label='Biform')
    ax2.set_xlabel(r'$G$', fontsize=12)
    ax2.set_ylabel('Manufacturer Profit', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_title('(b) Manufacturer Profit', fontsize=12, fontweight='bold')

    # Plot 3: Total profit
    ax3 = axes[1, 0]
    ax3.plot(G_vals, pi_total_n, color='#FF6F00', linewidth=2, label='Non-cooperative')
    ax3.plot(G_vals, phi_total, color='#00838F', linewidth=2, label='Biform')
    ax3.set_xlabel(r'$G$', fontsize=12)
    ax3.set_ylabel('Total Profit', fontsize=12)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.set_title('(c) Total Profit', fontsize=12, fontweight='bold')

    # Plot 4: Collection price p_R
    ax4 = axes[1, 1]
    ax4.plot(G_vals, pR_n, color='#FF6F00', linewidth=2, label='Non-cooperative')
    ax4.plot(G_vals, pR_c, color='#00838F', linewidth=2, label='Biform')
    ax4.set_xlabel(r'$G$', fontsize=12)
    ax4.set_ylabel(r'$p_R$', fontsize=12)
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    ax4.set_title('(d) Recycler Collection Price', fontsize=12, fontweight='bold')

    plt.tight_layout()
    OUTPUT_DIR = '/Users/zz/Library/CloudStorage/Dropbox/何门撸铁/_gym paper/zz05_合作非合作博弈/zz05_latexfile/simulation/figures_3d'
    plt.savefig(f'{OUTPUT_DIR}/g_multi_effect.png', bbox_inches='tight', facecolor='white', dpi=300)
    plt.close()
    print("g_multi_effect.png saved")