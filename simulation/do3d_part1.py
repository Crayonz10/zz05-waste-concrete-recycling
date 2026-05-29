#!/usr/bin/env python3
"""Part 1: w,s; alpha,beta; theta,mu_diff -> profit (4 cases each: M-Non, M-Bif, R-Non, R-Bif)"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.colors import LightSource

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'figure.dpi': 150,
    'savefig.dpi': 300,
})

OUTPUT_DIR = '/Users/zz/Library/CloudStorage/Dropbox/何门撸铁/_gym paper/zz05_合作非合作博弈/zz05_latexfile/simulation/figures_3d'

ALPHA = 1.5
BETA = 0.134
M = 32
W = 35
S = 87.5
MIU_M = 25
MIU_R = 44
C = 135000
THETA = 137.5
G = 300
PC_VAL = 65
E_VAL = 0.035

ls = LightSource(azdeg=315, altdeg=45)


def calc_non_coop(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    """Non-cooperative game (without R&D cooperation)"""
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
    Pi_MN = (th*k_N - pM - w - mM + s)*qM
    Pi_RN = (th*k_N - pR - m - mR + s)*qR + (w-m)*qM + th*th*qR*qR/(2*c) - pc*em
    return {'Pi_MN':Pi_MN,'Pi_RN':Pi_RN,'pM':pM,'pR':pR,'k_N':k_N,'qM':qM,'qR':qR}


def calc_biform(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    """Biform game (with R&D cooperation)"""
    den = (a-b)**3*(a+b)*th**4 - 4*c*(a-b)*(3*a*a-b*b)*th*th + 4*c*c*(4*a*a-b*b)
    if abs(den) < 1e-10: den = 1e-10
    num_pM = 4*c*c*(2*a*a*(s-w-mM)+a*b*(s-m-mR)-b*b*(w-m)) - 2*c*th*th*((a-b)*(a*a*(s-w-mM)-(a*a-a*b+b*b)*(w-m))-a*(a*a-a*b+b*b)*(mM-mR)) - 4*c*a*pc*e*(a-b)*(a*a-a*b+b*b)
    pM = num_pM / den
    num_pR = 4*c*c*a*(2*a*(s-m-mR)+b*(s-3*w+2*m-mM)) - 2*c*a*th*th*((a-b)*(a*(w-m)+b*(s-3*w+2*m-mM))+a*(a-2*b)*(mM-mR)) - 4*c*pc*e*(a-b)*(c*(2*a*a-b*b)-th*th*a*(a-b))
    pR = num_pR / den
    k_C = th*(a-b)*(pM + pR) / c
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    em = max(e*(a-b)*(pM+pR)-G, 0)
    phi_M = (s - pM - w - mM)*qM + th*th*qM*(qM + 2*qR)/(4*c)
    phi_R = (s - pR - m - mR)*qR + (w-m)*qM + th*th*(qR**2+(qM+qR)**2)/(4*c) - pc*em
    return {'phi_M':phi_M,'phi_R':phi_R,'pM':pM,'pR':pR,'k_C':k_C,'qM':qM,'qR':qR}


def make_plot(data_list, xl, yl, zl, filename, legend_patches=None):
    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='3d')

    xvals = data_list[0][0]
    yvals = data_list[0][1]
    XM, YM = np.meshgrid(xvals, yvals)

    all_z = []
    for xv, yv, zv, col in data_list:
        z = np.array(zv)
        all_z.extend(z[z>0].tolist())

    if all_z:
        z_min, z_max = min(all_z), max(all_z)
        z_range = max(z_max - z_min, 1)
        z_min -= z_range * 0.15
        z_max += z_range * 0.15

        for xv, yv, zv, col in data_list:
            z = np.array(zv)
            z = np.clip(z, z_min, z_max)
            ax.plot_surface(XM, YM, z, color=col, alpha=0.9,
                        rstride=5, cstride=5)

        ax.set_zlim(z_min, z_max)
        z_ticks = np.linspace(z_min, z_max, 6)
        ax.set_zticks(z_ticks)

    ax.view_init(elev=25, azim=-55)

    # Hide panes
    for pane in [ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane]:
        pane.fill = True
        pane.set_facecolor('white')
    ax.xaxis.pane.set_edgecolor('white')
    ax.yaxis.pane.set_edgecolor('white')
    ax.zaxis.pane.set_edgecolor('white')

    if legend_patches:
        ax.legend(handles=legend_patches, loc='upper left', fontsize=10)

    ax.set_xlabel(xl, fontsize=12)
    ax.set_ylabel(yl, fontsize=12)
    ax.set_zlabel(zl, fontsize=12)
    ax.tick_params(labelsize=9)

    plt.savefig(f'{OUTPUT_DIR}/{filename}', bbox_inches='tight', facecolor='white', dpi=300)
    plt.close()
    print(f"{filename} saved")


if __name__ == '__main__':
    a, b, th, c, s, w, m, mM, mR = ALPHA, BETA, THETA, C, S, W, M, MIU_M, MIU_R
    pc, e, G_val = PC_VAL, E_VAL, G

    # 1. W,S -> Profit (4 cases)
    w_vals = np.linspace(30, 50, 25)
    s_vals = np.linspace(70, 110, 25)

    pi_mn_non = np.zeros((25,25))
    pi_rn_non = np.zeros((25,25))
    phi_m_bif = np.zeros((25,25))
    phi_r_bif = np.zeros((25,25))

    for i in range(25):
        for j in range(25):
            r_non = calc_non_coop(a, b, th, c, s_vals[i], w_vals[j], m, mM, mR, pc, e, G_val)
            r_bif = calc_biform(a, b, th, c, s_vals[i], w_vals[j], m, mM, mR, pc, e, G_val)
            pi_mn_non[i,j] = max(r_non['Pi_MN'], 0)
            pi_rn_non[i,j] = max(r_non['Pi_RN'], 0)
            phi_m_bif[i,j] = max(r_bif['phi_M'], 0)
            phi_r_bif[i,j] = max(r_bif['phi_R'], 0)

    patches = [mp.Patch(color='#2E7D32', label='M-Non'), mp.Patch(color='#7B1FA2', label='M-Bif'),
              mp.Patch(color='#FF6F00', label='R-Non'), mp.Patch(color='#00838F', label='R-Bif')]
    make_plot([(w_vals, s_vals, pi_mn_non, '#2E7D32'), (w_vals, s_vals, phi_m_bif, '#7B1FA2'),
              (w_vals, s_vals, pi_rn_non, '#FF6F00'), (w_vals, s_vals, phi_r_bif, '#00838F')],
             r'$w$', r'$s$', 'Profit', 'ws_profit.png', patches)

    # 2. Alpha,Beta -> Profit (4 cases)
    a_vals = np.linspace(1.2, 2.0, 25)
    b_vals = np.linspace(0.08, 0.2, 25)

    pi_mn_non = np.zeros((25,25))
    pi_rn_non = np.zeros((25,25))
    phi_m_bif = np.zeros((25,25))
    phi_r_bif = np.zeros((25,25))

    for i in range(25):
        for j in range(25):
            r_non = calc_non_coop(a_vals[i], b_vals[j], th, c, s, w, m, mM, mR, pc, e, G_val)
            r_bif = calc_biform(a_vals[i], b_vals[j], th, c, s, w, m, mM, mR, pc, e, G_val)
            pi_mn_non[i,j] = max(r_non['Pi_MN'], 0)
            pi_rn_non[i,j] = max(r_non['Pi_RN'], 0)
            phi_m_bif[i,j] = max(r_bif['phi_M'], 0)
            phi_r_bif[i,j] = max(r_bif['phi_R'], 0)

    patches = [mp.Patch(color='#2E7D32', label='M-Non'), mp.Patch(color='#7B1FA2', label='M-Bif'),
              mp.Patch(color='#FF6F00', label='R-Non'), mp.Patch(color='#00838F', label='R-Bif')]
    make_plot([(a_vals, b_vals, pi_mn_non, '#2E7D32'), (a_vals, b_vals, phi_m_bif, '#7B1FA2'),
              (a_vals, b_vals, pi_rn_non, '#FF6F00'), (a_vals, b_vals, phi_r_bif, '#00838F')],
             r'$\alpha$', r'$\beta$', 'Profit', 'ab_profit.png', patches)

    # 3. Theta, Mu_diff -> Profit (4 cases)
    th_vals = np.linspace(100, 180, 25)
    mu_diff_vals = np.linspace(-30, 30, 25)  # mu_M - mu_R

    pi_mn_non = np.zeros((25,25))
    pi_rn_non = np.zeros((25,25))
    phi_m_bif = np.zeros((25,25))
    phi_r_bif = np.zeros((25,25))

    for i in range(25):
        for j in range(25):
            mM_val = 25 + mu_diff_vals[j]/2
            mR_val = 44 - mu_diff_vals[j]/2
            r_non = calc_non_coop(a, b, th_vals[i], c, s, w, m, mM_val, mR_val, pc, e, G_val)
            r_bif = calc_biform(a, b, th_vals[i], c, s, w, m, mM_val, mR_val, pc, e, G_val)
            pi_mn_non[i,j] = max(r_non['Pi_MN'], 0)
            pi_rn_non[i,j] = max(r_non['Pi_RN'], 0)
            phi_m_bif[i,j] = max(r_bif['phi_M'], 0)
            phi_r_bif[i,j] = max(r_bif['phi_R'], 0)

    patches = [mp.Patch(color='#2E7D32', label='M-Non'), mp.Patch(color='#7B1FA2', label='M-Bif'),
              mp.Patch(color='#FF6F00', label='R-Non'), mp.Patch(color='#00838F', label='R-Bif')]
    make_plot([(th_vals, mu_diff_vals, pi_mn_non, '#2E7D32'), (th_vals, mu_diff_vals, phi_m_bif, '#7B1FA2'),
              (th_vals, mu_diff_vals, pi_rn_non, '#FF6F00'), (th_vals, mu_diff_vals, phi_r_bif, '#00838F')],
             r'$\theta$', r'$\Delta\mu$', 'Profit', 'th_mu_profit.png', patches)

    print("Done!")