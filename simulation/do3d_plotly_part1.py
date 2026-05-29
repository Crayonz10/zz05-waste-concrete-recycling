#!/usr/bin/env python3
"""Part 1: w,s; alpha,beta; theta,mu_diff -> profit - Nature style"""
import numpy as np
import plotly.graph_objects as go

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
    Pi_MN = (th*k_N - pM - w - mM + s)*qM
    Pi_RN = (th*k_N - pR - m - mR + s)*qR + (w-m)*qM + th*th*qR*qR/(2*c) - pc*em
    return {'Pi_MN':Pi_MN,'Pi_RN':Pi_RN}


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
    phi_M = (s - pM - w - mM)*qM + th*th*qM*(qM + 2*qR)/(4*c)
    phi_R = (s - pR - m - mR)*qR + (w-m)*qM + th*th*(qR**2+(qM+qR)**2)/(4*c) - pc*em
    return {'phi_M':phi_M,'phi_R':phi_R}


# Morandi-style palette - muted, sophisticated colors
NAT_PALETTE = {
    'sage': '#8BA888',       # Sage green - M-Non
    'dusty_rose': '#C4A4A4',  # Dusty rose - R-Non
    'lavender': '#A99AA3',   # Dusty lavender - M-Bif
    'slate': '#7A9A9A',     # Slate blue - R-Bif
    'clay': '#B89882',       # Clay - single plots
    'mauve': '#9B8AA3',    # Muted mauve
}


def make_plot(data_list, xl, yl, zl, filename, eye_pos=None):
    if eye_pos is None:
        eye_pos = dict(x=1.5, y=1.5, z=0.75)

    fig = go.Figure()

    for xd, yd, zd, col, name in data_list:
        fig.add_trace(go.Surface(
            x=xd, y=yd, z=zd,
            colorscale=[[0, col], [1, col]],
            showscale=False,
            name=name,
            opacity=0.88,
            hoverinfo='none',
            contours={
                "x": {"show": False},
                "y": {"show": False},
                "z": {"show": False}
            }
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(
                title=dict(text=xl, font=dict(size=13, family='Times New Roman', color='#333333')),
                tickfont=dict(size=11, family='Times New Roman', color='#333333'),
                showgrid=False, showline=True, linewidth=1.5, linecolor='#333333',
                zeroline=False, showticklabels=True, tickmode='auto',
                backgroundcolor='rgba(0,0,0,0)',
                ticklen=5, tickwidth=1.5,
            ),
            yaxis=dict(
                title=dict(text=yl, font=dict(size=13, family='Times New Roman', color='#333333')),
                tickfont=dict(size=11, family='Times New Roman', color='#333333'),
                showgrid=False, showline=True, linewidth=1.5, linecolor='#333333',
                zeroline=False, showticklabels=True, tickmode='auto',
                backgroundcolor='rgba(0,0,0,0)',
                ticklen=5, tickwidth=1.5,
            ),
            zaxis=dict(
                title=dict(text=zl, font=dict(size=13, family='Times New Roman', color='#333333')),
                tickfont=dict(size=11, family='Times New Roman', color='#333333'),
                showgrid=False, showline=True, linewidth=1.5, linecolor='#333333',
                zeroline=False, showticklabels=True, tickmode='auto',
                backgroundcolor='rgba(0,0,0,0)',
                ticklen=5, tickwidth=1.5,
            ),
            camera=dict(eye=eye_pos, center=dict(x=0, y=0, z=-0.12)),
            aspectmode='cube',
        ),
        margin=dict(l=15, r=15, t=15, b=15),
        paper_bgcolor='white',
        plot_bgcolor='white',
    )

    shapes = []
    annotations = []
    legend_items = sorted(list(set([(d[3], d[4]) for d in data_list])), key=lambda x: x[1])

    for i, (color, name) in enumerate(legend_items):
        y_pos = 0.95 - i*0.055
        shapes.append(dict(
            type='rect',
            x0=0.01, x1=0.04,
            y0=y_pos-0.015, y1=y_pos+0.005,
            xref='paper', yref='paper',
            fillcolor=color,
            line=dict(color='white', width=0.5),
            layer='below',
        ))
        annotations.append(dict(
            x=0.045, y=y_pos,
            xref='paper', yref='paper',
            text=f'<b>{name}</b>',
            showarrow=False,
            font=dict(size=12, family='Times New Roman', color='#333333'),
            align='left',
        ))

    fig.update_layout(shapes=shapes, annotations=annotations)
    fig.write_image(f'{OUTPUT_DIR}/{filename}', width=1000, height=800, scale=2)
    print(f"{filename} saved")


if __name__ == '__main__':
    a, b, th, c, s, w, m, mM, mR = ALPHA, BETA, THETA, C, S, W, M, MIU_M, MIU_R
    pc, e, G_val = PC_VAL, E_VAL, G

    # 1. W,S -> Profit
    w_vals = np.linspace(30, 50, 30)
    s_vals = np.linspace(70, 110, 30)

    pi_mn_non = np.zeros((30,30))
    pi_rn_non = np.zeros((30,30))
    phi_m_bif = np.zeros((30,30))
    phi_r_bif = np.zeros((30,30))

    for i in range(30):
        for j in range(30):
            r_non = calc_non_coop(a, b, th, c, s_vals[i], w_vals[j], m, mM, mR, pc, e, G_val)
            r_bif = calc_biform(a, b, th, c, s_vals[i], w_vals[j], m, mM, mR, pc, e, G_val)
            pi_mn_non[i,j] = max(r_non['Pi_MN'], 0)
            pi_rn_non[i,j] = max(r_non['Pi_RN'], 0)
            phi_m_bif[i,j] = max(r_bif['phi_M'], 0)
            phi_r_bif[i,j] = max(r_bif['phi_R'], 0)

    data = [
        (w_vals, s_vals, pi_mn_non, NAT_PALETTE['sage'], 'M-Non'),
        (w_vals, s_vals, phi_m_bif, NAT_PALETTE['lavender'], 'M-Bif'),
        (w_vals, s_vals, pi_rn_non, NAT_PALETTE['dusty_rose'], 'R-Non'),
        (w_vals, s_vals, phi_r_bif, NAT_PALETTE['slate'], 'R-Bif'),
    ]
    make_plot(data, 'w', 's', 'Profit', 'ws_profit.png', eye_pos=dict(x=1.4, y=1.4, z=0.7))

    # 2. Alpha,Beta -> Profit
    a_vals = np.linspace(1.2, 2.0, 30)
    b_vals = np.linspace(0.08, 0.2, 30)

    pi_mn_non = np.zeros((30,30))
    pi_rn_non = np.zeros((30,30))
    phi_m_bif = np.zeros((30,30))
    phi_r_bif = np.zeros((30,30))

    for i in range(30):
        for j in range(30):
            r_non = calc_non_coop(a_vals[i], b_vals[j], th, c, s, w, m, mM, mR, pc, e, G_val)
            r_bif = calc_biform(a_vals[i], b_vals[j], th, c, s, w, m, mM, mR, pc, e, G_val)
            pi_mn_non[i,j] = max(r_non['Pi_MN'], 0)
            pi_rn_non[i,j] = max(r_non['Pi_RN'], 0)
            phi_m_bif[i,j] = max(r_bif['phi_M'], 0)
            phi_r_bif[i,j] = max(r_bif['phi_R'], 0)

    data = [
        (a_vals, b_vals, pi_mn_non, NAT_PALETTE['sage'], 'M-Non'),
        (a_vals, b_vals, phi_m_bif, NAT_PALETTE['lavender'], 'M-Bif'),
        (a_vals, b_vals, pi_rn_non, NAT_PALETTE['dusty_rose'], 'R-Non'),
        (a_vals, b_vals, phi_r_bif, NAT_PALETTE['slate'], 'R-Bif'),
    ]
    make_plot(data, 'α', 'β', 'Profit', 'ab_profit.png', eye_pos=dict(x=1.4, y=1.4, z=0.8))

    # 3. Theta, Mu_diff -> Profit
    th_vals = np.linspace(100, 180, 30)
    mu_diff_vals = np.linspace(0, 30, 30)

    pi_mn_non = np.zeros((30,30))
    pi_rn_non = np.zeros((30,30))
    phi_m_bif = np.zeros((30,30))
    phi_r_bif = np.zeros((30,30))

    for i in range(30):
        for j in range(30):
            mM_val = 34.5 - mu_diff_vals[j]/2
            mR_val = 34.5 + mu_diff_vals[j]/2
            r_non = calc_non_coop(a, b, th_vals[i], c, s, w, m, mM_val, mR_val, pc, e, G_val)
            r_bif = calc_biform(a, b, th_vals[i], c, s, w, m, mM_val, mR_val, pc, e, G_val)
            pi_mn_non[i,j] = max(r_non['Pi_MN'], 0)
            pi_rn_non[i,j] = max(r_non['Pi_RN'], 0)
            phi_m_bif[i,j] = max(r_bif['phi_M'], 0)
            phi_r_bif[i,j] = max(r_bif['phi_R'], 0)

    data = [
        (th_vals, mu_diff_vals, pi_mn_non, NAT_PALETTE['sage'], 'M-Non'),
        (th_vals, mu_diff_vals, phi_m_bif, NAT_PALETTE['lavender'], 'M-Bif'),
        (th_vals, mu_diff_vals, pi_rn_non, NAT_PALETTE['dusty_rose'], 'R-Non'),
        (th_vals, mu_diff_vals, phi_r_bif, NAT_PALETTE['slate'], 'R-Bif'),
    ]
    make_plot(data, 'θ', 'Δμ', 'Profit', 'th_mu_profit.png', eye_pos=dict(x=1.5, y=1.5, z=0.65))

    print("Done!")