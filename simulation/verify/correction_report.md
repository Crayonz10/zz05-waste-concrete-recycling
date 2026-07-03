# zz05 均衡价格修正报告

## 一、问题诊断摘要

正文 Proposition 1（非合作）和 Proposition 4（biform）的闭式解**都不正确**。经 sympy 数值验证：

| | 正文公式值 | 正确数值解 | FOC 残差 |
|---|---|---|---|
| $p_M^{N*}$ | 15.1087 | **14.3619** | -2.18 |
| $p_R^{N*}$ | 5.9191 | **5.7025** | -0.50 |
| $p_M^{C*}$ | 15.1087 (= N) | **15.0117** | -0.43 |
| $p_R^{C*}$ | 5.9191 (= N) | **6.4789** | +1.54 |

正文 biform 公式与非合作公式**完全相同**是 algebra 错误的副作用。

## 二、错误链条

### 1. 附录 A3/A4 推导（appendix.tex line 45）
```
∂k^N/∂p_M = p_c·γ·(α-β)/c            ← 错误（缺 -θβ/c）
∂k^N/∂p_R = (θ + p_c·γ·(α-β))/c      ← 错误（缺 α 因子）
```
正确：
```
∂k^N/∂p_M = [-θβ + p_c·γ·(α-β)]/c
∂k^N/∂p_R = [θα + p_c·γ·(α-β)]/c
```

### 2. 正文 Shapley 公式（manuscript.tex line 376-384）
**φ_M** 缺少碳排放耦合项：
- 正文: $\varphi_M = (s-p_M-w-\mu_M)q_M + \frac{\theta^2 q_M(q_M+2q_R)}{4c}$
- 正确: $\varphi_M = (s-p_M-w-\mu_M)q_M + \frac{\theta^2 q_M(q_M+2q_R)}{4c} + \mathbf{\frac{\theta p_c\gamma}{2c}(\alpha-\beta)(p_M+p_R) q_M}$

**φ_R** 碳项系数不对：
- 正文: $-p_c e_0 q_{tot} + \frac{p_c\gamma}{4c}(\alpha-\beta)^2(p_M+p_R)^2(\theta+p_c\gamma) + p_cG$
- 正确: $-p_c e_0 q_{tot} + \frac{\theta p_c\gamma}{2c}(\alpha-\beta)(p_M+p_R)(q_M+2q_R) + \mathbf{\frac{p_c^2\gamma^2}{c}(\alpha-\beta)^2(p_M+p_R)^2} + p_cG$

### 3. 附录 D1 (appendix.tex line 175-178)
biform FOC 缺 $p_c\gamma\theta$ 和 $p_c^2\gamma^2$ 项。

### 4. simulation/new_codes/plot_figures.py 第 85 行
原代码 `calculate_prices_C = calculate_prices_N`，导致"biform" 图实际上画的是非合作价格。

### 5. simulation/new_codes/plot_figures.py BASE_PARAMS
`c = 13500` 应该是 `c = 135000`（少了一个零），导致数值结果偏差大。

## 三、修正方案

闭式解过复杂（高阶多项式），建议改用**线性 FOC 矩阵**呈现：

### Proposition 1（非合作均衡价格）
R 独立决策 $k^N$，将其代入 $\Pi_M^N, \Pi_R^N$，得到关于 $(p_M, p_R)$ 的线性 2×2 系统：

```latex
\begin{equation}
\begin{pmatrix}
- 2 \alpha \left(- \alpha \gamma p_c \theta + \beta \gamma p_c \theta + \beta \theta^{2} + c\right) &
\alpha^{2} \gamma p_c \theta + \alpha^{2} \theta^{2} - 2 \alpha \beta \gamma p_c \theta + \beta^{2} \gamma p_c \theta + \beta^{2} \theta^{2} + \beta c \\
\alpha^{2} \gamma^{2} p_c^{2} + \alpha^{2} \gamma p_c \theta - 2 \alpha \beta \gamma^{2} p_c^{2} - 2 \alpha \beta \gamma p_c \theta - \alpha \beta \theta^{2} + \beta^{2} \gamma^{2} p_c^{2} + \beta^{2} \gamma p_c \theta + \beta c &
\alpha^{2} \gamma^{2} p_c^{2} + 2 \alpha^{2} \gamma p_c \theta + \alpha^{2} \theta^{2} - 2 \alpha \beta \gamma^{2} p_c^{2} - 2 \alpha \beta \gamma p_c \theta - 2 \alpha c + \beta^{2} \gamma^{2} p_c^{2}
\end{pmatrix}
\begin{pmatrix} p_M^{N*} \\ p_R^{N*} \end{pmatrix}
=
\begin{pmatrix}
- \alpha \left(- \mu_{M} + s - w\right) \\
\alpha e_0 p_c + \alpha m + \alpha \mu_R - \alpha s - \beta e_0 p_c - \beta m + \beta w
\end{pmatrix}
\end{equation}
```

应用 Cramer 法则可解出闭式（虽复杂，但至少是正确的）。

### Proposition 4（biform 均衡价格）
大联盟最优 $k^C$，Shapley 值 $\varphi_M, \varphi_R$ 作为支付函数：

```latex
\begin{equation}
\begin{pmatrix}
\alpha \left(2 \alpha \gamma p_c \theta + \alpha \theta^{2} - 2 \beta \gamma p_c \theta - 2 \beta \theta^{2} - 4 c\right) &
\alpha^{2} \gamma p_c \theta + \alpha^{2} \theta^{2} - 2 \alpha \beta \gamma p_c \theta - \alpha \beta \theta^{2} + \beta^{2} \gamma p_c \theta + \beta^{2} \theta^{2} + 2 \beta c \\
4 \alpha^{2} \gamma^{2} p_c^{2} + 3 \alpha^{2} \gamma p_c \theta + \alpha^{2} \theta^{2} - 8 \alpha \beta \gamma^{2} p_c^{2} - 6 \alpha \beta \gamma p_c \theta - 3 \alpha \beta \theta^{2} + 4 \beta^{2} \gamma^{2} p_c^{2} + 3 \beta^{2} \gamma p_c \theta + \beta^{2} \theta^{2} + 2 \beta c &
4 \alpha^{2} \gamma^{2} p_c^{2} + 4 \alpha^{2} \gamma p_c \theta + 2 \alpha^{2} \theta^{2} - 8 \alpha \beta \gamma^{2} p_c^{2} - 6 \alpha \beta \gamma p_c \theta - 2 \alpha \beta \theta^{2} - 4 \alpha c + 4 \beta^{2} \gamma^{2} p_c^{2} + 2 \beta^{2} \gamma p_c \theta + \beta^{2} \theta^{2}
\end{pmatrix}
\begin{pmatrix} p_M^{C*} \\ p_R^{C*} \end{pmatrix}
=
\begin{pmatrix}
- 2 \alpha \left(- \mu_{M} + s - w\right) \\
2 \alpha e_0 p_c + 2 \alpha m + 2 \alpha \mu_R - 2 \alpha s - 2 \beta e_0 p_c - 2 \beta m + 2 \beta w
\end{pmatrix}
\end{equation}
```
（这里常数项实际是 `α(...) - β(...)` 形式）

## 四、Baseline 数值解

```
非合作: p_M^N* = 14.36, p_R^N* = 5.70
Biform:  p_M^C* = 15.01, p_R^C* = 6.48
利润:    非合作 Π_M=292.85, Π_R=19541.68
         Biform  φ_M=298.77, φ_R=19569.66
Pareto:  M: True (↑2.02%), R: True (↑0.14%)
```

**好消息**：正确的 biform 模型**仍满足 Pareto 改进**，核心结论成立。

## 五、修正文件

| 文件 | 修改 |
|------|------|
| `simulation/new_codes/equilibria.py` | **新建**：修正后的均衡求解函数（FOC 矩阵形式） |
| `simulation/new_codes/plot_figures.py` | **修改**：导入 equilibria.py，修复 c=135000，使用正确的 Shapley 公式 |
| `simulation/verify/verify_equilibrium.py` | **新建**：sympy 验证脚本 |
| `manuscript.tex` | **待修改**：Prop 1 (lines 253-311)、Prop 4 (lines 401-435) 的闭式解 |
| `appendix.tex` | **待修改**：line 45 (∂k 偏导)、line 175-178 (D1 FOC) |

## 六、建议执行顺序

1. 用 `python3 simulation/verify/verify_equilibrium.py` 重新核对 baseline 数值
2. 用 sympy 生成闭式解（如果论文需要展示完整公式）
3. 修改 manuscript.tex 和 appendix.tex 中的公式
4. 修改后重新编译，验证 Figure 数据与正文描述一致
