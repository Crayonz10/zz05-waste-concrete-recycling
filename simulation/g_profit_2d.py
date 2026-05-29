#!/usr/bin/env python3
"""G -> Recycler profit (2D plot for biform vs non-cooperative)"""
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
    em = max(e*(a-b)*(pM+pR)-G, 0)
    Pi_RN = (th*k_N - pR - m - mR + s)*qR + (w-m)*qM + th*th*qR*qR/(2*c) - pc*em
    return {'Pi_RN': Pi_RN}


def calc_biform(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    den = (a-b)**3*(a+b)*th**4 - 4*c*(a-b)*(3*a*a-b*b)*th*th + 4*c*c*(4*a*a-b*b)
    if abs(den) < 1e-10: den = 1e-10
    num_pM = 4*c*c*(2*a*a*(s-w-mM)+a*b*(s-m-mR)-b*b*(w-m)) - 2*c*th*th*((a-b)*(a*a*(s-w-mM)-(a*a-a*b+b*b)*(w-m))-a*(a*a-a*b+b*b)*(mM-mR)) - 4*c*a*pc*e*(a-b)*(a*a-a*b+b*b)
    pM = num_pM / den
    num_pR = 4*c*c*a*(2*a*(s-m-mR)+b*(s-3*w+2*m-mM)) - 2*c*a*th*th*((a-b)*(a*(w-m)+b*(s-3*w+2*m-mM))+a*(a-2*b)*(mM-mR)) - 4*c*pc*e*(a-b)*(c*(2*a*a-b*b)-th*th*a*(a-b))
    pR = num_pR / den
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    em = max(e*(a-b)*(pM+pR)-G, 0)
    phi_R = (s - pR - m - mR)*qR + (w-m)*qM + th*th*(qR**2+(qM+qR)**2)/(4*c) - pc*em
    return {'phi_R': phi_R}


if __name__ == '__main__':
    a, b, th, c, s, w, m, mM, mR = ALPHA, BETA, THETA, C, S, W, M, MIU_M, MIU_R
    pc, e = PC_VAL, E_VAL

    G_vals = np.linspace(100, 500, 50)

    pi_rn = []
    phi_r = []
    for G_val in G_vals:
        r_non = calc_non_coop(a, b, th, c, s, w, m, mM, mR, pc, e, G_val)
        r_bif = calc_biform(a, b, th, c, s, w, m, mM, mR, pc, e, G_val)
        pi_rn.append(max(r_non['Pi_RN'], 0))
        phi_r.append(max(r_bif['phi_R'], 0))

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(G_vals, pi_rn, color='#FF6F00', linewidth=2, label='Non-cooperative')
    ax.plot(G_vals, phi_r, color='#00838F', linewidth=2, label='Biform')
    ax.set_xlabel(r'$G$', fontsize=13)
    ax.set_ylabel('Recycler Profit', fontsize=13)
    ax.legend(fontsize=11)
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    OUTPUT_DIR = '/Users/zz/Library/CloudStorage/Dropbox/何门撸铁/_gym paper/zz05_合作非合作博弈/zz05_latexfile/simulation/figures_3d'
    plt.savefig(f'{OUTPUT_DIR}/g_profit_2d.png', bbox_inches='tight', facecolor='white', dpi=300)
    plt.close()
    print("g_profit_2d.png saved")