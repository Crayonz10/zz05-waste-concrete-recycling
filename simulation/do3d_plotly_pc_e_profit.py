#!/usr/bin/env python3
"""3D Plots"""
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 如果不使用自动保存，这个路径就不需要了，但我为你保留在代码里
OUTPUT_DIR = '/Users/zz/Library/CloudStorage/Dropbox/何门撸铁/_gym paper/zz05_合作非合作博弈/zz05_latexfile/simulation/figures_3d'

ALPHA = 1.5
BETA = 0.134
M_VAL = 32
W_VAL = 35
S_VAL = 87.5
MIU_M = 25
MIU_R = 44
C_VAL = 135000
THETA = 137.5
G_VAL = 300


def calc_denom(a, b, th, c):
    d = (a-b)**3*(a+b)*th**4 - 4*c*(a-b)*(3*a*a-b*b)*th*th + 4*c*c*(4*a*a-b*b)
    if abs(d) < 1e-10:
        d = 1e-10
    return d


def calc_pM_star(a, b, th, c, s, w, m, mM, mR, pc, e):
    den = calc_denom(a, b, th, c)
    term1 = 4*c*c * (2*a*a*(s-w-mM) + a*b*(s-m-mR) - b*b*(w-m))
    term2_inner = (a-b)*(a*a*(s-w-mM) - (a*a-a*b+b*b)*(w-m)) - a*(a*a-a*b+b*b)*(mM-mR)
    term2 = 2*c*th*th * term2_inner
    term3 = 4*c*a*pc*e*(a-b)*(a*a-a*b+b*b)
    num = term1 - term2 - term3
    return num / den


def calc_pR_star(a, b, th, c, s, w, m, mM, mR, pc, e):
    den = calc_denom(a, b, th, c)
    term1 = 4*c*c*a * (2*a*(s-m-mR) + b*(s-3*w+2*m-mM))
    term2_inner = (a-b)*(a*(w-m) + b*(s-3*w+2*m-mM)) + a*(a-2*b)*(mM-mR)
    term2 = 2*c*a*th*th * term2_inner
    term3 = 4*c*pc*e*(a-b) * (c*(2*a*a-b*b) - th*th*a*(a-b))
    num = term1 - term2 - term3
    return num / den


def calc_profits(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    pM = calc_pM_star(a, b, th, c, s, w, m, mM, mR, pc, e)
    pR = calc_pR_star(a, b, th, c, s, w, m, mM, mR, pc, e)
    k_N = th*(a*pR - b*pM) / c
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    em = max(e*(a-b)*(pM+pR) - G, 0)
    Pi_MN = (th*k_N - pM - w - mM + s) * qM
    Pi_RN = (th*k_N - pR - m - mR + s)*qR + (w-m)*qM + th*th*qR*qR/(2*c) - pc*em
    phi_M = (s - pM - w - mM)*qM + th*th*qM*(qM + 2*qR)/(4*c)
    phi_R = (s - pR - m - mR)*qR + (w-m)*qM + th*th*(qR**2 + (qM+qR)**2)/(4*c) - pc*em
    return Pi_MN, Pi_RN, phi_M, phi_R


if __name__ == "__main__":
    a, b, th, c, s, w, m, mM, mR, G = ALPHA, BETA, THETA, C_VAL, S_VAL, W_VAL, M_VAL, MIU_M, MIU_R, G_VAL
    pc_vals = np.linspace(30, 90, 35)
    e_vals = np.linspace(0.01, 0.065, 35)

    Pi_MN = np.zeros((35, 35))
    Pi_MC = np.zeros((35, 35))
    Pi_RN = np.zeros((35, 35))
    Pi_RC = np.zeros((35, 35))

    print("Computing...")
    for i in range(35):
        for j in range(35):
            pc, e = pc_vals[j], e_vals[i]
            Pi_MN[i,j], Pi_RN[i,j], Pi_MC[i,j], Pi_RC[i,j] = calc_profits(a, b, th, c, s, w, m, mM, mR, pc, e, G)

    Pi_MN = np.clip(Pi_MN, 0, None)
    Pi_MC = np.clip(Pi_MC, 0, None)
    Pi_RN = np.clip(Pi_RN, 0, None)
    Pi_RC = np.clip(Pi_RC, 0, None)

    COLORS_M = {"Non": "#B85A38", "Bif": "#3A6B8C"}
    COLORS_R = {"Non": "#8B6B6B", "Bif": "#4A7C5A"}
    TF = "Times New Roman"
    TC = "#222222"

    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "surface"}, {"type": "surface"}]],
        subplot_titles=["(a) Manufacturer", "(b) Recycler"],
        horizontal_spacing=0.05
    )

    t1 = go.Surface(x=pc_vals, y=e_vals, z=Pi_MN, colorscale=[[0, COLORS_M["Non"]], [1, COLORS_M["Non"]]], showscale=False, opacity=0.9)
    t2 = go.Surface(x=pc_vals, y=e_vals, z=Pi_MC, colorscale=[[0, COLORS_M["Bif"]], [1, COLORS_M["Bif"]]], showscale=False, opacity=0.9)
    t3 = go.Surface(x=pc_vals, y=e_vals, z=Pi_RN, colorscale=[[0, COLORS_R["Non"]], [1, COLORS_R["Non"]]], showscale=False, opacity=0.9)
    t4 = go.Surface(x=pc_vals, y=e_vals, z=Pi_RC, colorscale=[[0, COLORS_R["Bif"]], [1, COLORS_R["Bif"]]], showscale=False, opacity=0.9)

    fig.add_trace(t1, row=1, col=1)
    fig.add_trace(t2, row=1, col=1)
    fig.add_trace(t3, row=1, col=2)
    fig.add_trace(t4, row=1, col=2)

    # ------------------------------------------------------------------
    # 开始布局配置：针对浏览器显示进行优化
    # ------------------------------------------------------------------
    shapes = []
    annotations = []

    # === 左图 (Manufacturer) 左上角图例 ===
    # 因为在浏览器里横向空间很大，0.01 是真正的最左边，0.5 是一半
    left_rect_x = 0.02
    left_text_x = 0.035

    shapes.append(dict(type="rect", x0=left_rect_x, x1=left_rect_x+0.015, y0=0.97, y1=0.99, xref="paper", yref="paper", fillcolor=COLORS_M["Non"], line=dict(width=0)))
    annotations.append(dict(x=left_text_x, y=0.98, xref="paper", yref="paper", text="Non-cooperative", showarrow=False, font=dict(family=TF, size=14, color=TC), align="left", xanchor="left"))

    shapes.append(dict(type="rect", x0=left_rect_x, x1=left_rect_x+0.015, y0=0.92, y1=0.94, xref="paper", yref="paper", fillcolor=COLORS_M["Bif"], line=dict(width=0)))
    annotations.append(dict(x=left_text_x, y=0.93, xref="paper", yref="paper", text="Biform", showarrow=False, font=dict(family=TF, size=14, color=TC), align="left", xanchor="left"))

    # === 右图 (Recycler) 左上角图例 ===
    right_rect_x = 0.52
    right_text_x = 0.535

    shapes.append(dict(type="rect", x0=right_rect_x, x1=right_rect_x+0.015, y0=0.97, y1=0.99, xref="paper", yref="paper", fillcolor=COLORS_R["Non"], line=dict(width=0)))
    annotations.append(dict(x=right_text_x, y=0.98, xref="paper", yref="paper", text="Non-cooperative", showarrow=False, font=dict(family=TF, size=14, color=TC), align="left", xanchor="left"))

    shapes.append(dict(type="rect", x0=right_rect_x, x1=right_rect_x+0.015, y0=0.92, y1=0.94, xref="paper", yref="paper", fillcolor=COLORS_R["Bif"], line=dict(width=0)))
    annotations.append(dict(x=right_text_x, y=0.93, xref="paper", yref="paper", text="Biform", showarrow=False, font=dict(family=TF, size=14, color=TC), align="left", xanchor="left"))

    # 相机视角稍微拉远一点，方便你在网页里看全
    common_scene = dict(
        xaxis=dict(title=dict(text="pc", font=dict(size=12, family=TF, color=TC)), tickfont=dict(size=10, family=TF, color=TC), showgrid=False, showline=True, linewidth=1, linecolor="#444", backgroundcolor="white"),
        yaxis=dict(title=dict(text="e", font=dict(size=12, family=TF, color=TC)), tickfont=dict(size=10, family=TF, color=TC), showgrid=False, showline=True, linewidth=1, linecolor="#444", backgroundcolor="white"),
        zaxis=dict(title=dict(text="Profit", font=dict(size=12, family=TF, color=TC)), tickfont=dict(size=10, family=TF, color=TC), showgrid=False, showline=True, linewidth=1, linecolor="#444", backgroundcolor="white"),
        camera=dict(eye=dict(x=1.8, y=1.8, z=0.8)), 
        aspectmode="cube", 
        bgcolor="white"
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        # 移除了固定的 width 和 height，让图形自适应浏览器窗口大小
        margin=dict(l=20, r=20, t=80, b=20), # 顶部留足 80 的空间给图例和标题
        shapes=shapes,
        annotations=annotations,
        scene=common_scene,
        scene2=common_scene
    )

    # 放大子图标题，确保在浏览器里清晰
    for annotation in fig['layout']['annotations']:
        if annotation['text'] in ["(a) Manufacturer", "(b) Recycler"]:
            annotation['font'] = dict(family=TF, size=18, color=TC)
            annotation['y'] = 1.05  # 将标题稍微往上抬，和图例拉开层次

    print("Opening plot in browser...")
    # 改为直接在浏览器展示
    fig.show()