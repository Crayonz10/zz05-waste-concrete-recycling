"""Plot Figure 1 (abc) for the biform game paper.

Three 3D subplots comparing non-cooperative profits (Pi_M^N, Pi_R^N) with
biform Shapley allocations (phi_M, phi_R). Surfaces use the Morandi palette
with carefully tuned transparency so all four layers remain visible.

Run from simulation/scripts/. Saves PNG to ../figures/Figure_1.png at 300 dpi.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import matplotlib.lines as mlines

# ---------- Style ----------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['axes.grid'] = False
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

COLORS = {
    'Biform_M':   '#4A7B76',   # Soft Teal
    'Biform_R':   '#5B7B9A',   # Muted Blue
    'NonCoop_M':  '#B56C60',   # Dusty Rose
    'NonCoop_R':  '#D3A273',   # Warm Sand
}

# Visualisation: the cooperative surplus (phi - Pi^N) is tiny (~5 units for
# M, ~19 for R) compared to total profits (~250 and ~19,500). On a linear
# z-axis the biform and non-coop surfaces of each pair occupy the same
# visible height. We amplify the within-pair gap by GAP_AMP so all four
# surfaces read as distinct filled layers. The amplification factor is
# constant for every (x, y) point, so the SHAPES of the surfaces and their
# relative ordering (phi > Pi^N, R > M) are preserved.
GAP_AMP = 120
ALPHA_NC = 0.55

GRID_N = 40
OUT_DIR = os.path.join('..', 'figures')
os.makedirs(OUT_DIR, exist_ok=True)

PARAMS = dict(alpha=1.5, beta=0.134, m=32, w=35, s=87.5,
              muM=25, muR=44, c=135000, theta=137.5,
              pc=65, G=300, e0=0.035, gamma=0.015)


# ---------- Equilibrium solver (vectorised closed-form) ----------
def calculate_equilibrium(alpha=PARAMS['alpha'], beta=PARAMS['beta'], m=PARAMS['m'],
                          w=PARAMS['w'], s=PARAMS['s'], muM=PARAMS['muM'],
                          muR=PARAMS['muR'], c=PARAMS['c'], theta=PARAMS['theta'],
                          pc=PARAMS['pc'], G=PARAMS['G'], e0=PARAMS['e0'],
                          gamma=PARAMS['gamma']):
    D = (alpha**4 * gamma * pc * theta * (gamma * pc + theta)**2
         + alpha**3 * (-2 * beta * gamma * pc * theta * (gamma * pc + theta)**2
                       - beta * theta**4 - 2 * c * (gamma * pc + theta)**2
                       - 4 * c * gamma * pc * theta - beta * gamma * pc * theta**3)
         + alpha**2 * (3 * beta * c * (gamma * pc + theta)**2 + 4 * c**2)
         + alpha * beta**2 * c * theta * (4 * gamma * pc + theta)
         + 2 * alpha * beta**3 * gamma * pc * theta * (gamma * pc + theta)**2
         + alpha * beta**3 * theta**4 + alpha * beta**3 * gamma * pc * theta**3
         - beta**4 * gamma * pc * theta * (gamma * pc + theta)**2
         - beta**3 * c * (gamma * pc + theta)**2 - beta**2 * c**2)

    N_M_N = (c**2 * (2 * alpha**2 * (s - w - muM) - alpha * beta * (m + muR + e0 * pc - s)
                     + beta**2 * (m + e0 * pc - w))
             + c * (alpha**3 * (gamma**2 * pc**2 * (muM - s + w)
                                + gamma * pc * theta * (2 * muM - muR - s + 2 * w - m)
                                - theta**2 * (m - muM + muR - w)
                                - e0 * pc * theta * (gamma * pc + theta))
                    + alpha**2 * beta * (2 * gamma**2 * pc**2 * (-muM + s - w)
                                         + gamma * pc * theta * (3 * m - 2 * muM + 2 * muR - 3 * w)
                                         + theta**2 * (m - w)
                                         + e0 * pc * theta * (3 * gamma * pc + theta))
                    + alpha * beta**2 * (gamma**2 * pc**2 * (muM - s + w)
                                         + gamma * pc * theta * (-muR + s + 2 * w - 3 * m)
                                         - theta**2 * (m + muR - s)
                                         - e0 * pc * theta * (3 * gamma * pc + theta))
                    + beta**3 * (gamma * pc * theta * (m - w) + theta**2 * (m - w)
                                 + e0 * pc * theta * (gamma * pc + theta))))

    N_R_N = (c**2 * (2 * alpha**2 * (s - m - muR - e0 * pc)
                     + alpha * beta * (2 * m - muM + s - 3 * w + 2 * e0 * pc))
             + c * (alpha**3 * (2 * e0 * gamma * pc**2 * theta
                                + gamma**2 * pc**2 * (-muM + s - w)
                                + gamma * pc * theta * (2 * m - muM + 2 * muR - s - w))
                    + alpha**2 * beta * (-2 * e0 * pc * theta * (2 * gamma * pc + theta)
                                         + 2 * gamma**2 * pc**2 * (muM - s + w)
                                         + gamma * pc * theta * (2 * muM - 2 * muR - 4 * m + 4 * w)
                                         - theta**2 * (2 * m - muM + 2 * muR - s - w))
                    + alpha * beta**2 * (2 * e0 * pc * theta * (gamma * pc + theta)
                                         + gamma**2 * pc**2 * (-muM + s - w)
                                         + gamma * pc * theta * (-muM + s + 2 * m - 3 * w)
                                         + 2 * theta**2 * (m - w))))

    pM_N = N_M_N / D
    pR_N = N_R_N / D

    qM_N = alpha * pM_N - beta * pR_N
    qR_N = alpha * pR_N - beta * pM_N
    k_N = (theta * (alpha * pR_N - beta * pM_N)
           + pc * gamma * (alpha - beta) * (pM_N + pR_N)) / c

    Pi_M_N = (theta * k_N - pM_N - w - muM + s) * qM_N
    Pi_R_N = ((theta * k_N - pR_N - m - muR + s) * qR_N
              + (w - m) * qM_N
              - (theta * qR_N + pc * gamma * (alpha - beta) * (pM_N + pR_N))**2 / (2 * c)
              - pc * ((e0 - gamma * k_N) * (alpha - beta) * (pM_N + pR_N) - G))

    D_C = (alpha**4 * (2 * gamma**3 * pc**3 * theta + 5 * gamma**2 * pc**2 * theta**2
                       + 4 * gamma * pc * theta**3 + theta**4)
           + alpha**3 * beta * (-4 * gamma**3 * pc**3 * theta - 10 * gamma**2 * pc**2 * theta**2
                                - 8 * gamma * pc * theta**3 - 2 * theta**4)
           + alpha**3 * c * (-8 * gamma**2 * pc**2 - 24 * gamma * pc * theta - 12 * theta**2)
           + alpha**2 * beta * c * (12 * gamma**2 * pc**2 + 24 * gamma * pc * theta + 12 * theta**2)
           + 16 * alpha**2 * c**2
           + alpha * beta**3 * (4 * gamma**3 * pc**3 * theta + 10 * gamma**2 * pc**2 * theta**2
                                + 8 * gamma * pc * theta**3 + 2 * theta**4)
           + alpha * beta**2 * c * theta * (8 * gamma * pc + 4 * theta)
           - beta**4 * (2 * gamma**3 * pc**3 * theta + 5 * gamma**2 * pc**2 * theta**2
                        + 4 * gamma * pc * theta**3 + theta**4)
           - beta**3 * c * (4 * gamma**2 * pc**2 + 8 * gamma * pc * theta + 4 * theta**2)
           - 4 * beta**2 * c**2)

    N_M_C = (c**2 * (8 * alpha**2 * (s - m - muM)
                     - 4 * alpha * beta * (m + muR + e0 * pc - s)
                     + 4 * beta**2 * (m + e0 * pc - w))
             + c * (alpha**3 * (-2 * e0 * gamma * pc**2 * theta - 2 * e0 * pc * theta**2
                                + 4 * gamma**2 * pc**2 * (m + muM - s)
                                + 2 * gamma * pc * theta * (3 * m + 4 * muM - muR - 3 * s)
                                + 2 * theta**2 * (m + 2 * muM - muR - s))
                    + alpha**2 * beta * (6 * e0 * gamma * pc**2 * theta + 4 * e0 * pc * theta**2
                                         - 8 * gamma**2 * pc**2 * (m + muM - s)
                                         + 2 * gamma * pc * theta * (-3 * m - 6 * muM + 2 * muR + 4 * s - w)
                                         + 2 * theta**2 * (-2 * muM + muR + s - w))
                    + alpha * beta**2 * (-6 * e0 * gamma * pc**2 * theta - 4 * e0 * pc * theta**2
                                         + 4 * gamma**2 * pc**2 * (m + muM - s)
                                         + 2 * gamma * pc * theta * (-m + 2 * muM - muR - s + 2 * w)
                                         + 2 * theta**2 * (-m + muM - muR + w))
                    + beta**3 * (2 * e0 * gamma * pc**2 * theta + 2 * e0 * pc * theta**2
                                 + 2 * gamma * pc * theta * (m - w)
                                 + 2 * theta**2 * (m - w))))

    N_R_C = (c**2 * (8 * alpha**2 * (s - m - muR - e0 * pc)
                     + 4 * alpha * beta * (m - muM + s - 2 * w + 2 * e0 * pc))
             + c * (alpha**3 * (4 * e0 * gamma * pc**2 * theta + 2 * e0 * pc * theta**2
                                - 4 * gamma**2 * pc**2 * (m + muM - s)
                                + 2 * gamma * pc * theta * (-m - 3 * muM + 2 * muR + s)
                                + 2 * theta**2 * (-muM + muR))
                    + alpha**2 * beta * (-8 * e0 * gamma * pc**2 * theta - 6 * e0 * pc * theta**2
                                         + 8 * gamma**2 * pc**2 * (m + muM - s)
                                         + 2 * gamma * pc * theta * (2 * m + 6 * muM - 2 * muR - 4 * s + 2 * w)
                                         + 2 * theta**2 * (3 * muM - 2 * muR - s + w))
                    + alpha * beta**2 * (4 * e0 * gamma * pc**2 * theta + 4 * e0 * pc * theta**2
                                         - 4 * gamma**2 * pc**2 * (m + muM - s)
                                         + 2 * gamma * pc * theta * (-m - 3 * muM + 3 * s - 2 * w)
                                         + 2 * theta**2 * (m - muM + s - 2 * w))))

    pM_C = N_M_C / D_C
    pR_C = N_R_C / D_C

    qM_C = alpha * pM_C - beta * pR_C
    qR_C = alpha * pR_C - beta * pM_C
    qT_C = (alpha - beta) * (pM_C + pR_C)
    k_C = ((theta + pc * gamma) * qT_C) / c
    n_C = (1
           - (theta**2 * qM_C * (3 * qM_C + 2 * qR_C))
             / (2 * (theta + pc * gamma)**2 * qT_C**2)
           - (theta * pc * gamma * qM_C)
             / ((theta + pc * gamma)**2 * qT_C))

    phi_M = ((s - pM_C - w - muM) * qM_C
             + (theta**2 * qM_C * (qM_C + 2 * qR_C)) / (4 * c)
             + (theta * pc * gamma * qT_C * qM_C) / (2 * c))
    phi_R = ((s - pR_C - m - muR) * qR_C
             + (w - m) * qM_C
             + (theta**2 * qR_C**2) / (4 * c)
             + (theta**2 * qT_C**2) / (4 * c)
             + (theta * pc * gamma * qT_C * (qM_C + 2 * qR_C)) / (2 * c)
             + (pc**2 * gamma**2 * qT_C**2) / (2 * c)
             - pc * e0 * qT_C
             + pc * G)

    return dict(pM_N=pM_N, pR_N=pR_N, qM_N=qM_N, qR_N=qR_N, k_N=k_N,
                Pi_M_N=Pi_M_N, Pi_R_N=Pi_R_N,
                pM_C=pM_C, pR_C=pR_C, qM_C=qM_C, qR_C=qR_C,
                k_C=k_C, n_C=n_C, phi_M=phi_M, phi_R=phi_R)


# ---------- 3D axes helpers ----------
def style_3d_box(ax):
    """Hide the 3D bounding box and pane edges; keep only the three axes."""
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('none')
    ax.yaxis.pane.set_edgecolor('none')
    ax.zaxis.pane.set_edgecolor('none')
    ax.xaxis.pane.set_linewidth(0)
    ax.yaxis.pane.set_linewidth(0)
    ax.zaxis.pane.set_linewidth(0)
    ax.grid(False)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.line.set_linewidth(1.0)
        axis.line.set_color('black')


def proxy_swatch_filled(label, color):
    """Filled-square legend proxy for filled surfaces."""
    return mlines.Line2D([], [], color=color, marker='s', markersize=9,
                         linestyle='None', markeredgecolor='none', label=label)


def add_panel_label(ax, label):
    ax.text2D(0.5, 0.94, label, transform=ax.transAxes,
              ha='center', va='top', fontsize=13, fontweight='bold')


# ---------- Figure 1 ----------
def plot_figure1():
    fig = plt.figure(figsize=(18, 5.5))

    configs = [
        ('(a)', r'$\alpha$', r'$\beta$',
         (np.linspace(1.1, 1.8, GRID_N), np.linspace(0.05, 0.4, GRID_N)),
         dict(alpha='x', beta='y')),
        ('(b)', r'$w$', r'$s$',
         (np.linspace(20, 60, GRID_N), np.linspace(50, 120, GRID_N)),
         dict(w='x', s='y')),
        ('(c)', r'$\theta$', r'$\Delta\mu \;(=\mu_R-\mu_M)$',
         (np.linspace(100, 200, GRID_N), np.linspace(5, 40, GRID_N)),
         dict(theta='x', muR=lambda v: 25 + v)),
    ]

    view = dict(elev=30, azim=-65)

    for i, (tag, xlabel, ylabel, (xrng, yrng), sweep) in enumerate(configs, start=1):
        ax = fig.add_subplot(1, 3, i, projection='3d')
        style_3d_box(ax)

        X, Y = np.meshgrid(xrng, yrng)
        kwargs = {}
        for arg, axis in sweep.items():
            if axis == 'x':
                kwargs[arg] = X
            elif axis == 'y':
                kwargs[arg] = Y
            else:
                kwargs[arg] = axis(Y)
        res = calculate_equilibrium(**kwargs)

        # Cooperative surplus amplification for visualisation (see GAP_AMP).
        surplus_M = res['phi_M'] - res['Pi_M_N']
        surplus_R = res['phi_R'] - res['Pi_R_N']
        phi_M_vis = res['Pi_M_N'] + GAP_AMP * surplus_M
        phi_R_vis = res['Pi_R_N'] + GAP_AMP * surplus_R

        # Non-coop profits: filled semi-transparent surfaces (the lower pair).
        ax.plot_surface(X, Y, res['Pi_M_N'], color=COLORS['NonCoop_M'],
                        alpha=ALPHA_NC, edgecolor='none',
                        rstride=1, cstride=1, shade=True)
        ax.plot_surface(X, Y, res['Pi_R_N'], color=COLORS['NonCoop_R'],
                        alpha=ALPHA_NC, edgecolor='none',
                        rstride=1, cstride=1, shade=True)

        # Biform profits: filled surfaces with amplified surplus so the
        # layer sits visibly above its non-coop counterpart.
        ax.plot_surface(X, Y, phi_M_vis, color=COLORS['Biform_M'],
                        alpha=ALPHA_NC, edgecolor='none',
                        rstride=1, cstride=1, shade=True)
        ax.plot_surface(X, Y, phi_R_vis, color=COLORS['Biform_R'],
                        alpha=ALPHA_NC, edgecolor='none',
                        rstride=1, cstride=1, shade=True)

        ax.set_xlabel(xlabel, labelpad=10)
        ax.set_ylabel(ylabel, labelpad=10)
        ax.set_zlabel('Profit', labelpad=6)
        ax.view_init(**view)

        proxies = [
            proxy_swatch_filled(r'$\Pi_M^{N*}$', COLORS['NonCoop_M']),
            proxy_swatch_filled(r'$\Pi_R^{N*}$', COLORS['NonCoop_R']),
            proxy_swatch_filled(r'$\varphi_M$',  COLORS['Biform_M']),
            proxy_swatch_filled(r'$\varphi_R$',  COLORS['Biform_R']),
        ]
        ax.legend(handles=proxies, loc='upper left',
                  bbox_to_anchor=(0.0, 1.0), frameon=False,
                  fontsize=11, handletextpad=0.4, borderpad=0.2,
                  labelspacing=0.25)
        add_panel_label(ax, tag)

    plt.tight_layout(pad=1.5, w_pad=2.0)
    out = os.path.join(OUT_DIR, 'Figure_1.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved {out}')


if __name__ == '__main__':
    plot_figure1()
