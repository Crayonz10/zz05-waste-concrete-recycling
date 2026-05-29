#!/usr/bin/env python3
"""3D plots - Nature journal style"""
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


def calc_n(pM, pR, a, b):
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    num = 2*qR**2 + 2*qM*qR - qM**2
    denom = 2*((a-b)*(pM+pR))**2
    return max(num/denom, 0) if abs(denom) > 1e-10 else 0


def calc_all(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    den = (a-b)**3*(a+b)*th**4 - 4*c*(a-b)*(3*a*a-b*b)*th*th + 4*c*c*(4*a*a-b*b)
    if abs(den) < 1e-10: den = 1e-10
    num_pM = 4*c*c*(2*a*a*(s-w-mM)+a*b*(s-m-mR)-b*b*(w-m)) - 2*c*th*th*((a-b)*(a*a*(s-w-mM)-(a*a-a*b+b*b)*(w-m))-a*(a*a-a*b+b*b)*(mM-mR)) - 4*c*a*pc*e*(a-b)*(a*a-a*b+b*b)
    pM = num_pM / den
    num_pR = 4*c*c*a*(2*a*(s-m-mR)+b*(s-3*w+2*m-mM)) - 2*c*a*th*th*((a-b)*(a*(w-m)+b*(s-3*w+2*m-mM))+a*(a-2*b)*(mM-mR)) - 4*c*pc*e*(a-b)*(c*(2*a*a-b*b)-th*th*a*(a-b))
    pR = num_pR / den
    k_N = th*(a*pR - b*pM) / c
    k_C = th*(a-b)*(pM + pR) / c
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    em = max(e*(a-b)*(pM+pR)-G, 0)
    Pi_MN = (th*k_N - pM - w - mM + s)*qM
    Pi_RN = (th*k_N - pR - m - mR + s)*qR + (w-m)*qM + th*th*qR*qR/(2*c) - pc*em
    phi_M = (s - pM - w - mM)*qM + th*th*qM*(qM + 2*qR)/(4*c)
    phi_R = (s - pR - m - mR)*qR + (w-m)*qM + th*th*(qR**2+(qM+qR)**2)/(4*c) - pc*em
    n_val = calc_n(pM, pR, a, b)
    return {'Pi_MN':Pi_MN,'Pi_RN':Pi_RN,'phi_M':phi_M,'phi_R':phi_R,'pM':pM,'pR':pR,'k_C':k_C,'qM':qM,'qR':qR,'n':n_val}


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
        eye_pos = dict(x=1.5, y=1.5, z=0.8)

    fig = go.Figure()

    # Surface smoothing for cleaner look
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
                "z": {"show": False, "highlight": False}
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

    # Clean legend with colored markers
    shapes = []
    annotations = []
    legend_items = sorted(list(set([(d[3], d[4]) for d in data_list])), key=lambda x: x[1])

    # Better spacing and positioning
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

    pc_val = np.linspace(30, 90, 35)
    e_val = np.linspace(0.01, 0.016, 35)

    # pc,e PROFIT
    pi_mn = np.zeros((35,35))
    pi_rn = np.zeros((35,35))
    phi_m = np.zeros((35,35))
    phi_r = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            pi_mn[i,j] = max(r['Pi_MN'], 0)
            pi_rn[i,j] = max(r['Pi_RN'], 0)
            phi_m[i,j] = max(r['phi_M'], 0)
            phi_r[i,j] = max(r['phi_R'], 0)

    data = [
        (pc_val, e_val, pi_mn, NAT_PALETTE['sage'], 'M-Non'),
        (pc_val, e_val, pi_rn, NAT_PALETTE['dusty_rose'], 'R-Non'),
        (pc_val, e_val, phi_m, NAT_PALETTE['lavender'], 'M-Bif'),
        (pc_val, e_val, phi_r, NAT_PALETTE['slate'], 'R-Bif'),
    ]
    make_plot(data, 'p_c', 'e', 'Profit', 'pc_e_profit.png', eye_pos=dict(x=1.4, y=1.4, z=0.7))

    # pc,e PRICE
    pm = np.zeros((35,35))
    pr = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            pm[i,j] = r['pM']
            pr[i,j] = r['pR']

    data = [
        (pc_val, e_val, pm, NAT_PALETTE['sage'], 'M'),
        (pc_val, e_val, pr, NAT_PALETTE['dusty_rose'], 'R'),
    ]
    make_plot(data, 'p_c', 'e', 'Price', 'pc_e_price.png', eye_pos=dict(x=1.5, y=1.5, z=0.8))

    # pc,e QUANTITY
    qm = np.zeros((35,35))
    qr = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            qm[i,j] = max(r['qM'], 0)
            qr[i,j] = max(r['qR'], 0)

    data = [
        (pc_val, e_val, qm, NAT_PALETTE['sage'], 'M'),
        (pc_val, e_val, qr, NAT_PALETTE['dusty_rose'], 'R'),
    ]
    make_plot(data, 'p_c', 'e', 'Quantity', 'pc_e_quantity.png', eye_pos=dict(x=1.4, y=1.4, z=0.75))

    # pc,e K
    k = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            k[i,j] = max(r['k_C'], 0)

    data = [(pc_val, e_val, k, NAT_PALETTE['slate'], 'k')]
    make_plot(data, 'p_c', 'e', 'k', 'pc_e_k.png', eye_pos=dict(x=1.5, y=1.5, z=0.7))

    # pc,e N
    n = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            n[i,j] = max(r['n'], 0)

    data = [(pc_val, e_val, n, NAT_PALETTE['mauve'], 'n')]
    make_plot(data, 'p_c', 'e', 'n', 'pc_e_n.png', eye_pos=dict(x=1.5, y=1.5, z=0.75))

    print("Done!")