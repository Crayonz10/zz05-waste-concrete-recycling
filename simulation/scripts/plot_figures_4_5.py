"""Plot Figures 4 and 5 for the biform game paper.

2D sensitivity plots for biform equilibrium variables vs carbon trading
price p_c (Figure 4) and baseline unit emissions e_0 (Figure 5).

Each figure has three subplots: prices (a), quantities (b), and a dual-axis
subplot for n^C* (cost share, left) and k^C* (right) on (c). Parameter
ranges are restricted to the region where the unconstrained optimum
n^C* stays non-negative; beyond that point the n ∈ [0, 1] modelling
constraint binds at the boundary and the cooperative cost-share allocation
collapses to n = 0, which is not informative for a sensitivity plot.

Both n^C* and k^C* are displayed on [0, 1] axes using constant scaling
factors (×10 for n, ×30 for k) so the curves fit the same unit interval.
Axis labels are kept as n^C* and k^C* without scaling notation; the
scaling is described in the manuscript text.

Run from simulation/scripts/. Saves PNGs to ../figures/ at 300 dpi.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from plot_figure1 import calculate_equilibrium, COLORS

OUT_DIR = os.path.join('..', 'figures')
os.makedirs(OUT_DIR, exist_ok=True)


# ---------- Style ----------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['axes.grid'] = False
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

MARKER_SIZE = 6
MARKER_EDGE_LW = 1.0
LINE_LW = 1.6
N_POINTS = 15
N_SCALE = 10   # n^C* actual range ~0.007-0.06 → display ~0.07-0.6 on [0, 1]
K_SCALE = 30   # k^C* actual range ~0.028-0.032 → display ~0.84-0.96 on [0, 1]

# Common y-tick positions for the [0, 1] dual-axis subplot (c)
SHARED_YTICKS = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]


# ---------- Legend style shared by all panels ----------
_LEG_KW = dict(frameon=True, framealpha=0.92, edgecolor='0.8',
               fontsize=11, handletextpad=0.5, borderpad=0.35,
               labelspacing=0.3)


def _panel(ax, tag):
    ax.text(0.5, 1.02, tag, transform=ax.transAxes,
            ha='center', va='bottom', fontsize=13, fontweight='bold')


def _scatter_line(ax, x, y, color, marker, label, linestyle='-'):
    """Draw a scatter+line series and return the handle for the legend."""
    h, = ax.plot(x, y, color=color, marker=marker,
                 markersize=MARKER_SIZE, markeredgecolor=color,
                 markerfacecolor='white', markeredgewidth=MARKER_EDGE_LW,
                 linestyle=linestyle, linewidth=LINE_LW, label=label)
    return h


# ---------- Reusable figure builder ----------
def _plot_sensitivity(fig, x_var, x_label, vec):
    """Layout the three-panel sensitivity figure.

    (a) prices, (b) quantities, (c) n^C* (left) and k^C* (right) on [0, 1].
    """
    res = calculate_equilibrium(**{x_var: vec})

    # --- (a) collection prices ---
    ax1 = fig.add_subplot(1, 3, 1)
    h1a = _scatter_line(ax1, vec, res['pM_C'], COLORS['Biform_M'],
                        marker='o', label=r'$p_M^{C*}$')
    h1b = _scatter_line(ax1, vec, res['pR_C'], COLORS['Biform_R'],
                        marker='s', label=r'$p_R^{C*}$')
    ax1.set_xlabel(x_label)
    ax1.set_ylabel('Collection price')
    ax1.legend(handles=[h1a, h1b], loc='lower left',
               bbox_to_anchor=(0.02, 0.02), **_LEG_KW)
    _panel(ax1, '(a)')

    # --- (b) quantities ---
    ax2 = fig.add_subplot(1, 3, 2)
    h2a = _scatter_line(ax2, vec, res['qM_C'], COLORS['Biform_M'],
                        marker='o', label=r'$q_M^{C*}$')
    h2b = _scatter_line(ax2, vec, res['qR_C'], COLORS['Biform_R'],
                        marker='s', label=r'$q_R^{C*}$')
    h2c = _scatter_line(ax2, vec, res['qM_C'] + res['qR_C'],
                        COLORS['NonCoop_R'], marker='^',
                        label=r'$q_{total}^{C*}$', linestyle='--')
    ax2.set_xlabel(x_label)
    ax2.set_ylabel('Collection quantity')
    ax2.legend(handles=[h2a, h2b, h2c], loc='lower left',
               bbox_to_anchor=(0.02, 0.02), **_LEG_KW)
    _panel(ax2, '(b)')

    # --- (c) n^C* and k^C* on twin axes, both on [0, 1] ---
    ax3a = fig.add_subplot(1, 3, 3)
    n_display = res['n_C'] * N_SCALE
    h3a, = ax3a.plot(vec, n_display, color=COLORS['Biform_M'],
                     marker='o', markersize=MARKER_SIZE,
                     markeredgecolor=COLORS['Biform_M'],
                     markerfacecolor='white', markeredgewidth=MARKER_EDGE_LW,
                     linestyle='-', linewidth=LINE_LW,
                     label=r'$n^{C*}$')
    ax3a.set_xlabel(x_label)
    ax3a.set_ylabel(r'$n^{C*}$', color=COLORS['Biform_M'])
    ax3a.tick_params(axis='y', labelcolor=COLORS['Biform_M'])
    ax3a.set_ylim(0.0, 1.0)
    ax3a.set_yticks(SHARED_YTICKS)

    ax3b = ax3a.twinx()
    k_display = res['k_C'] * K_SCALE
    h3b, = ax3b.plot(vec, k_display, color=COLORS['Biform_R'],
                     marker='s', markersize=MARKER_SIZE,
                     markeredgecolor=COLORS['Biform_R'],
                     markerfacecolor='white', markeredgewidth=MARKER_EDGE_LW,
                     linestyle='--', linewidth=LINE_LW,
                     label=r'$k^{C*}$')
    ax3b.set_ylabel(r'$k^{C*}$', color=COLORS['Biform_R'])
    ax3b.tick_params(axis='y', labelcolor=COLORS['Biform_R'])
    ax3b.set_ylim(0.0, 1.0)
    ax3b.set_yticks(SHARED_YTICKS)

    # Lower-left legend: descending curves leave this corner empty.
    ax3a.legend(handles=[h3a, h3b], loc='lower left',
                bbox_to_anchor=(0.02, 0.02), **_LEG_KW)
    _panel(ax3a, '(c)')


# ---------- Figure 4: sensitivity to p_c ----------
def plot_figure4():
    fig = plt.figure(figsize=(16, 5))
    # Restricted to pc in [0, 50]: keeps n^C* > 0 throughout.
    pc_vec = np.linspace(0, 50, N_POINTS)
    _plot_sensitivity(fig, x_var='pc', x_label=r'$p_c$', vec=pc_vec)
    plt.tight_layout(pad=1.5, w_pad=2.0)
    out = os.path.join(OUT_DIR, 'Figure_4.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved {out}')


# ---------- Figure 5: sensitivity to e_0 ----------
def plot_figure5():
    fig = plt.figure(figsize=(16, 5))
    # Restricted to e0 in [0.01, 0.03]: keeps n^C* > 0 throughout.
    e0_vec = np.linspace(0.01, 0.03, N_POINTS)
    _plot_sensitivity(fig, x_var='e0', x_label=r'$e_0$', vec=e0_vec)
    plt.tight_layout(pad=1.5, w_pad=2.0)
    out = os.path.join(OUT_DIR, 'Figure_5.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved {out}')


if __name__ == '__main__':
    plot_figure4()
    plot_figure5()