"""Plot Figures 2 and 3 for the biform game paper.

Uses the same Morandi palette, no-bounding-box 3D axes, compact upper-left
legend, and (for Figure 3) the same GAP_AMP amplification trick as Figure 1
so all four profit surfaces read as distinct filled layers.

Run from simulation/scripts/. Saves PNGs to ../figures/ at 300 dpi.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import matplotlib.lines as mlines

from plot_figure1 import (calculate_equilibrium, COLORS, GRID_N,
                          style_3d_box, proxy_swatch_filled, add_panel_label,
                          GAP_AMP, ALPHA_NC)

OUT_DIR = os.path.join('..', 'figures')
os.makedirs(OUT_DIR, exist_ok=True)


# ---------- Figure 2: Conversion rate k (3D, 1x2) ----------
def plot_figure2():
    """k^N (non-coop conversion) vs k^C (biform conversion).

    No amplification needed: k^C is consistently 3-5x larger than k^N
    across the full grid, so the two surfaces are well separated.
    """
    fig = plt.figure(figsize=(12, 5.5))

    configs = [
        ('(a)', r'$\theta$', r'$\gamma$',
         (np.linspace(100, 200, GRID_N), np.linspace(0, 0.05, GRID_N)),
         dict(theta='x', gamma='y')),
        ('(b)', r'$\alpha$', r'$\beta$',
         (np.linspace(1.1, 1.8, GRID_N), np.linspace(0.05, 0.4, GRID_N)),
         dict(alpha='x', beta='y')),
    ]

    view = dict(elev=30, azim=-65)

    for i, (tag, xlabel, ylabel, (xrng, yrng), sweep) in enumerate(configs, start=1):
        ax = fig.add_subplot(1, 2, i, projection='3d')
        style_3d_box(ax)

        X, Y = np.meshgrid(xrng, yrng)
        kwargs = {arg: (X if axis == 'x' else Y) for arg, axis in sweep.items()}
        res = calculate_equilibrium(**kwargs)

        # Non-coop (lower) and biform (higher) — both filled, no mesh lines.
        # Display k on [0, 1] by scaling ×10 so tick labels read as 0.1, 0.2, ...
        K_DISP = 10
        k_N_disp = res['k_N'] * K_DISP
        k_C_disp = res['k_C'] * K_DISP
        ax.plot_surface(X, Y, k_N_disp, color=COLORS['NonCoop_R'],
                        alpha=ALPHA_NC, edgecolor='none',
                        rstride=1, cstride=1, shade=True)
        ax.plot_surface(X, Y, k_C_disp, color=COLORS['Biform_M'],
                        alpha=ALPHA_NC, edgecolor='none',
                        rstride=1, cstride=1, shade=True)

        ax.set_xlabel(xlabel, labelpad=12)
        ax.set_ylabel(ylabel, labelpad=12)
        # Per-panel z-axis upper bound: 0.7 for theta-gamma plane, 0.5 for
        # alpha-beta plane so the k surfaces sit closer to the z-axis top.
        if i == 1:
            ax.set_zlim(0.0, 0.7)
            ax.set_zticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
            ax.set_zlabel('$k$', labelpad=10)
        else:
            ax.set_zlim(0.0, 0.5)
            ax.set_zticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
            ax.set_zlabel('$k$', labelpad=10)
        ax.view_init(elev=35, azim=-60)

        proxies = [
            proxy_swatch_filled(r'$k^{N*}$', COLORS['NonCoop_R']),
            proxy_swatch_filled(r'$k^{C*}$', COLORS['Biform_M']),
        ]
        ax.legend(handles=proxies, loc='upper left',
                  bbox_to_anchor=(0.0, 1.0), frameon=False,
                  fontsize=12, handletextpad=0.4, borderpad=0.2,
                  labelspacing=0.3)
        add_panel_label(ax, tag)

    plt.tight_layout(pad=1.0, w_pad=0.5)
    out = os.path.join(OUT_DIR, 'Figure_2.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved {out}')


# ---------- Figure 3: Cap-and-Trade impact on profit (3D, 1x2) ----------
def plot_figure3():
    """Pi_M^N / Pi_R^N (non-coop) vs phi_M / phi_R (biform Shapley allocation)
    over the (p_c, e_0) grid.

    Same M/R clustering issue as Figure 1, so GAP_AMP amplification is needed.
    """
    fig = plt.figure(figsize=(12, 5.5))

    Px, E0x = np.meshgrid(np.linspace(0, 120, GRID_N),
                          np.linspace(0.01, 0.1, GRID_N))
    res = calculate_equilibrium(pc=Px, e0=E0x)

    # Amplify the cooperative surplus so all four surfaces read distinctly.
    phi_M_vis = res['Pi_M_N'] + GAP_AMP * (res['phi_M'] - res['Pi_M_N'])
    phi_R_vis = res['Pi_R_N'] + GAP_AMP * (res['phi_R'] - res['Pi_R_N'])

    view = dict(elev=30, azim=-65)

    # (a) M's profit
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    style_3d_box(ax1)
    ax1.plot_surface(Px, E0x, res['Pi_M_N'], color=COLORS['NonCoop_M'],
                     alpha=ALPHA_NC, edgecolor='none',
                     rstride=1, cstride=1, shade=True)
    ax1.plot_surface(Px, E0x, phi_M_vis, color=COLORS['Biform_M'],
                     alpha=ALPHA_NC, edgecolor='none',
                     rstride=1, cstride=1, shade=True)
    ax1.set_xlabel(r'$p_c$', labelpad=10)
    ax1.set_ylabel(r'$e_0$', labelpad=10)
    ax1.set_zlabel(r"$\Pi_M$", labelpad=6)
    ax1.view_init(**view)
    proxies_M = [
        proxy_swatch_filled(r'$\Pi_M^{N*}$', COLORS['NonCoop_M']),
        proxy_swatch_filled(r'$\varphi_M$',  COLORS['Biform_M']),
    ]
    ax1.legend(handles=proxies_M, loc='upper left',
               bbox_to_anchor=(0.0, 1.0), frameon=False,
               fontsize=12, handletextpad=0.4, borderpad=0.2,
               labelspacing=0.3)
    add_panel_label(ax1, '(a)')

    # (b) R's profit
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    style_3d_box(ax2)
    ax2.plot_surface(Px, E0x, res['Pi_R_N'], color=COLORS['NonCoop_R'],
                     alpha=ALPHA_NC, edgecolor='none',
                     rstride=1, cstride=1, shade=True)
    ax2.plot_surface(Px, E0x, phi_R_vis, color=COLORS['Biform_R'],
                     alpha=ALPHA_NC, edgecolor='none',
                     rstride=1, cstride=1, shade=True)
    ax2.set_xlabel(r'$p_c$', labelpad=10)
    ax2.set_ylabel(r'$e_0$', labelpad=10)
    ax2.set_zlabel(r"$\Pi_R$", labelpad=6)
    ax2.view_init(**view)
    proxies_R = [
        proxy_swatch_filled(r'$\Pi_R^{N*}$', COLORS['NonCoop_R']),
        proxy_swatch_filled(r'$\varphi_R$',  COLORS['Biform_R']),
    ]
    ax2.legend(handles=proxies_R, loc='upper left',
               bbox_to_anchor=(0.0, 1.0), frameon=False,
               fontsize=12, handletextpad=0.4, borderpad=0.2,
               labelspacing=0.3)
    add_panel_label(ax2, '(b)')

    plt.tight_layout(pad=1.5, w_pad=2.0)
    out = os.path.join(OUT_DIR, 'Figure_3.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved {out}')


if __name__ == '__main__':
    plot_figure2()
    plot_figure3()
