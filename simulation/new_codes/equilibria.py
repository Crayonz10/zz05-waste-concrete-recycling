"""
zz05 修正后的均衡价格求解函数

非合作博弈 (Proposition 1):
    由 ∂Π_M^N/∂p_M = 0, ∂Π_R^N/∂p_R = 0 求解
    k^N = [θ·q_R + p_c·γ·q_tot] / c  (R 独立决策)

Biform 博弈 (Proposition 4):
    Shapley 值 φ_M, φ_R 作为非合作阶段的支付函数
    由 ∂φ_M/∂p_M = 0, ∂φ_R/∂p_R = 0 求解
    k^C = (θ + p_c·γ)·q_tot / c  (大联盟最优)

所有函数返回 (p_M*, p_R*)，失败时返回 (nan, nan)。
"""
import numpy as np


def _solve_2x2(a11, a12, b1, a21, a22, b2):
    """Solve 2x2 linear system. Returns (x, y) or (nan, nan) if singular."""
    det = a11 * a22 - a12 * a21
    if abs(det) < 1e-15:
        return np.nan, np.nan
    x = (b1 * a22 - b2 * a12) / det
    y = (a11 * b2 - a21 * b1) / det
    return x, y


def calc_prices_N(alpha, beta, m, w, s, mu_M, mu_R, c, theta, pc, e0, gamma):
    """
    非合作博弈均衡价格 (Prop 1)
    k^N(p_M, p_R) = [θ·(α p_R - β p_M) + p_c·γ·(α-β)·(p_M+p_R)] / c

    将 k^N 代入 Π_M^N, Π_R^N 求 FOC，得到关于 (p_M, p_R) 的线性 2×2 系统。

    系统(乘以c以简化):
      a11·p_M + a12·p_R = b1
      a21·p_M + a22·p_R = b2

    其中:
      a11 = 2α·[αγ p_c θ - βγ p_c θ - βθ² - c] / c
      a12 = [α²γ p_c θ + α²θ² - 2αβγ p_c θ + β²γ p_c θ + β²θ² + βc] / c
      b1  = -α(s - w - μ_M)
      a21 = [α²γ² p_c² + α²γ p_c θ - 2αβγ² p_c² - 2αβγ p_c θ - αβθ²
             + β²γ² p_c² + β²γ p_c θ + βc] / c
      a22 = [α²γ² p_c² + 2α²γ p_c θ + α²θ² - 2αβγ² p_c² - 2αβγ p_c θ
             - 2αc + β²γ² p_c²] / c
      b2  = -[α(e_0 p_c + m + μ_R - s) - β(e_0 p_c + m - w)]
    """
    # Build coefficients
    a11 = 2*alpha * (alpha*gamma*pc*theta - beta*gamma*pc*theta - beta*theta**2 - c) / c
    a12 = (alpha**2*gamma*pc*theta + alpha**2*theta**2
           - 2*alpha*beta*gamma*pc*theta
           + beta**2*gamma*pc*theta + beta**2*theta**2 + beta*c) / c
    b1 = -alpha * (s - w - mu_M)
    a21 = (alpha**2*gamma**2*pc**2 + alpha**2*gamma*pc*theta
           - 2*alpha*beta*gamma**2*pc**2 - 2*alpha*beta*gamma*pc*theta
           - alpha*beta*theta**2
           + beta**2*gamma**2*pc**2 + beta**2*gamma*pc*theta + beta*c) / c
    a22 = (alpha**2*gamma**2*pc**2 + 2*alpha**2*gamma*pc*theta + alpha**2*theta**2
           - 2*alpha*beta*gamma**2*pc**2 - 2*alpha*beta*gamma*pc*theta
           - 2*alpha*c
           + beta**2*gamma**2*pc**2) / c
    b2 = alpha*(e0*pc + m + mu_R - s) - beta*(e0*pc + m - w)

    return _solve_2x2(a11, a12, b1, a21, a22, b2)


def calc_prices_C(alpha, beta, m, w, s, mu_M, mu_R, c, theta, pc, e0, gamma, G):
    """
    Biform 博弈均衡价格 (Prop 4)
    Shapley 值 φ_M, φ_R 作为支付函数，求 Nash 均衡

    k^C(p_M, p_R) = (θ + p_c·γ)·(α-β)·(p_M+p_R) / c  (大联盟最优)

    Shapley 值:
      φ_M = ½V({M}) + ½[V({M,R}) - V({R})]
      φ_R = ½V({R}) + ½[V({M,R}) - V({M})]

    系统(乘以 2c 以简化):
      a11·p_M + a12·p_R = b1
      a21·p_M + a22·p_R = b2
    """
    a11 = alpha * (2*alpha*gamma*pc*theta + alpha*theta**2
                   - 2*beta*gamma*pc*theta - 2*beta*theta**2 - 4*c) / (2*c)
    a12 = (alpha**2*gamma*pc*theta + alpha**2*theta**2
           - 2*alpha*beta*gamma*pc*theta - alpha*beta*theta**2
           + beta**2*gamma*pc*theta + beta**2*theta**2 + 2*beta*c) / (2*c)
    b1 = -alpha * (s - w - mu_M)
    a21 = (4*alpha**2*gamma**2*pc**2 + 3*alpha**2*gamma*pc*theta + alpha**2*theta**2
           - 8*alpha*beta*gamma**2*pc**2 - 6*alpha*beta*gamma*pc*theta
           - 3*alpha*beta*theta**2
           + 4*beta**2*gamma**2*pc**2 + 3*beta**2*gamma*pc*theta
           + beta**2*theta**2 + 2*beta*c) / (2*c)
    a22 = (4*alpha**2*gamma**2*pc**2 + 4*alpha**2*gamma*pc*theta + 2*alpha**2*theta**2
           - 8*alpha*beta*gamma**2*pc**2 - 6*alpha*beta*gamma*pc*theta
           - 2*alpha*beta*theta**2 - 4*alpha*c
           + 4*beta**2*gamma**2*pc**2 + 2*beta**2*gamma*pc*theta
           + beta**2*theta**2) / (2*c)
    b2 = alpha*(e0*pc + m + mu_R - s) - beta*(e0*pc + m - w)

    return _solve_2x2(a11, a12, b1, a21, a22, b2)


def calc_k_N(p_M, p_R, alpha, beta, theta, pc, gamma, c):
    """非合作 k*"""
    if c == 0:
        return np.nan
    return (theta * (alpha*p_R - beta*p_M) + pc*gamma*(alpha-beta)*(p_M + p_R)) / c


def calc_k_C(p_M, p_R, alpha, beta, theta, pc, gamma, c):
    """Biform 大联盟 k*"""
    if c == 0:
        return np.nan
    return (theta + pc*gamma) * (alpha-beta) * (p_M + p_R) / c


def calc_phi_M(p_M, p_R, alpha, beta, theta, s, w, mu_M, c):
    """
    Shapley 值 φ_M(p_M, p_R)
    φ_M = (s - p_M - w - μ_M)q_M + θ²q_M(q_M + 2q_R)/(4c)
          + θ p_c γ (α-β)(p_M+p_R) q_M / (2c)

    第三项为碳排放耦合项 (正文中缺失)。
    """
    q_M = alpha*p_M - beta*p_R
    q_R = alpha*p_R - beta*p_M
    q_tot = (alpha-beta)*(p_M + p_R)
    return ((s - p_M - w - mu_M) * q_M
            + theta**2 * q_M * (q_M + 2*q_R) / (4*c)
            + theta * pc * gamma * q_tot * q_M / (2*c))


def calc_phi_R(p_M, p_R, alpha, beta, theta, s, w, m, mu_R, pc, e0, gamma, c, G):
    """
    Shapley 值 φ_R(p_M, p_R) — 完整版（含正确碳排放项）
    """
    q_M = alpha*p_M - beta*p_R
    q_R = alpha*p_R - beta*p_M
    q_tot = (alpha-beta)*(p_M + p_R)
    return ((s - p_R - m - mu_R) * q_R + (w - m) * q_M
            + theta**2 * (q_R**2 + (q_M + q_R)**2) / (4*c)
            - pc * e0 * q_tot
            + theta * pc * gamma * q_tot * (q_M + 2*q_R) / (2*c)
            + pc**2 * gamma**2 * q_tot**2 / c
            + pc * G)


def calc_n_C(p_M, p_R, alpha, beta):
    """Biform 阶段 R 分担 R&D 投资比例 n"""
    q_M = alpha*p_M - beta*p_R
    q_R = alpha*p_R - beta*p_M
    denom = 2 * ((alpha-beta)*(p_M + p_R))**2
    if denom == 0:
        return np.nan
    return (2*q_R**2 + 2*q_M*q_R - q_M**2) / denom


if __name__ == '__main__':
    # 自检
    BASE = dict(alpha=1.5, beta=0.134, m=32, w=35, s=87.5, mu_M=25, mu_R=44,
                c=135000, theta=137.5, pc=65, e0=0.035, gamma=0.015, G=300)
    p_M_N, p_R_N = calc_prices_N(**{k: v for k, v in BASE.items() if k != 'G'})
    p_M_C, p_R_C = calc_prices_C(**BASE)
    print(f"非合作: p_M={p_M_N:.4f}, p_R={p_R_N:.4f}")
    print(f"Biform: p_M={p_M_C:.4f}, p_R={p_R_C:.4f}")
    print(f"(预期: 14.3619, 5.7025 / 15.0117, 6.4789)")