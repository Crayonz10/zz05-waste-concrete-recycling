#!/usr/bin/env python3
"""3D plots using Plotly - no grid lines"""
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


def make_plot(data_list, xl, yl, zl, filename):
    x = data_list[0][0]
    y = data_list[0][1]

    fig = go.Figure()

    for xd, yd, zd, col, name in data_list:
        fig.add_trace(go.Surface(
            x=xd, y=yd, z=zd,
            colorscale=[[0, col], [1, col]],
            showscale=False,
            name=name,
            opacity=0.9,
            hoverinfo='none',
        ))

    camera = dict(eye=dict(x=1.5, y=1.5, z=1.2))

    fig.update_layout(
        scene=dict(
            xaxis_title=xl,
            yaxis_title=yl,
            zaxis_title=zl,
            camera=camera,
            xaxis=dict(
                showgrid=False, showline=True, linewidth=1, linecolor='black',
                zeroline=False, showticklabels=True, tickmode='auto',
                title=dict(font=dict(size=12)),
                backgroundcolor='white',
            ),
            yaxis=dict(
                showgrid=False, showline=True, linewidth=1, linecolor='black',
                zeroline=False, showticklabels=True, tickmode='auto',
                title=dict(font=dict(size=12)),
                backgroundcolor='white',
            ),
            zaxis=dict(
                showgrid=False, showline=True, linewidth=1, linecolor='black',
                zeroline=False, showticklabels=True, tickmode='auto',
                title=dict(font=dict(size=12)),
                backgroundcolor='white',
            ),
            aspectmode='cube',
        ),
        margin=dict(l=50, r=50, t=50, b=50),
        paper_bgcolor='white',
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(x=0.02, y=0.98, font=dict(size=11), bgcolor='rgba(255,255,255,0.8)'),
    )

    fig.write_image(f'{OUTPUT_DIR}/{filename}', width=1200, height=900, scale=2)
    print(f"{filename} saved")


if __name__ == '__main__':
    a, b, th, c, s, w, m, mM, mR = ALPHA, BETA, THETA, C, S, W, M, MIU_M, MIU_R

    pc_val = np.linspace(30, 90, 35)
    e_val = np.linspace(0.01, 0.06, 35)

    # PC,E PROFIT
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
        (pc_val, e_val, pi_mn, '#2E7D32', 'M-Non'),
        (pc_val, e_val, pi_rn, '#FF6F00', 'R-Non'),
        (pc_val, e_val, phi_m, '#7B1FA2', 'M-Bif'),
        (pc_val, e_val, phi_r, '#00838F', 'R-Bif'),
    ]
    make_plot(data, 'p_c', 'e', 'Profit', 'pc_e_profit.png')

    # PC,E PRICE
    pm = np.zeros((35,35))
    pr = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            pm[i,j] = r['pM']
            pr[i,j] = r['pR']

    data = [
        (pc_val, e_val, pm, '#2E7D32', 'M'),
        (pc_val, e_val, pr, '#E65100', 'R'),
    ]
    make_plot(data, r'$p_c$', r'$e$', 'Price', 'pc_e_price.png')

    # PC,E QUANTITY
    qm = np.zeros((35,35))
    qr = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            qm[i,j] = max(r['qM'], 0)
            qr[i,j] = max(r['qR'], 0)

    data = [
        (pc_val, e_val, qm, '#2E7D32', 'M'),
        (pc_val, e_val, qr, '#E65100', 'R'),
    ]
    make_plot(data, r'$p_c$', r'$e$', 'Quantity', 'pc_e_quantity.png')

    # PC,E K
    k = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            k[i,j] = max(r['k_C'], 0)

    data = [(pc_val, e_val, k, '#00838F', 'k')]
    make_plot(data, r'$p_c$', r'$e$', r'$k$', 'pc_e_k.png')

    # PC,E N
    n = np.zeros((35,35))
    for i in range(35):
        for j in range(35):
            r = calc_all(a, b, th, c, s, w, m, mM, mR, pc_val[j], e_val[i], G)
            n[i,j] = max(r['n'], 0)

    data = [(pc_val, e_val, n, '#7B1FA2', 'n')]
    make_plot(data, r'$p_c$', r'$e$', r'$n$', 'pc_e_n.png')

    print("Done!")