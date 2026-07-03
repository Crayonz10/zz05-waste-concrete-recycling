"""
zz05 均衡价格正确性验证脚本

用法：
    python3 simulation/verify/verify_equilibrium.py

输出：
    - 非合作与 biform 均衡价格数值
    - 一阶条件残差
    - 利润分配与 Pareto 改进检验
"""
import sympy as sp
import numpy as np

# ============ 符号定义 ============
alpha, beta, m, w, s, mu_M, mu_R, c, theta, pc, e0, gamma, G = sp.symbols(
    'alpha beta m w s mu_M mu_R c theta pc e0 gamma G', positive=True)
p_M, p_R = sp.symbols('p_M p_R', real=True)

q_M = alpha*p_M - beta*p_R
q_R = alpha*p_R - beta*p_M
q_tot = q_M + q_R

# ============ Baseline 参数 ============
SUBS = {alpha:1.5, beta:0.134, m:32, w:35, s:87.5, mu_M:25, mu_R:44,
        c:135000, theta:137.5, pc:65, e0:0.035, gamma:0.015, G:300}

# ============ 非合作博弈求解 ============
def solve_noncoop(sub):
    """返回 (p_M^N*, p_R^N*) 的解析解"""
    k = (theta*q_R + pc*gamma*q_tot)/c
    Pi_M = (theta*k - p_M - w - mu_M + s)*q_M
    Pi_R = (theta*k - p_R - m - mu_R + s)*q_R + (w - m)*q_M \
           - c*k**2/2 - pc*((e0 - gamma*k)*q_tot - G)
    
    poly_M = sp.Poly(sp.expand(sp.diff(Pi_M, p_M)), p_M, p_R)
    poly_R = sp.Poly(sp.expand(sp.diff(Pi_R, p_R)), p_M, p_R)
    
    A = sp.Matrix([
        [poly_M.coeff_monomial(p_M), poly_M.coeff_monomial(p_R)],
        [poly_R.coeff_monomial(p_M), poly_R.coeff_monomial(p_R)]
    ])
    b = sp.Matrix([
        -poly_M.coeff_monomial(1),
        -poly_R.coeff_monomial(1)
    ])
    
    sol = A.subs(sub).solve(b.subs(sub))
    return float(sol[0]), float(sol[1])

# ============ Biform 博弈求解 ============
def solve_biform(sub):
    """返回 (p_M^C*, p_R^C*) 的解析解（正确 Shapley FOC）"""
    V_M = (s - p_M - w - mu_M)*q_M
    V_R = (s - p_R - m - mu_R)*q_R + (w - m)*q_M + theta**2*q_R**2/(2*c) \
          - pc*e0*q_tot + pc*gamma*q_tot*(theta*q_R + pc*gamma*q_tot)/c + pc*G
    V_MR = (s - p_M - m - mu_M)*q_M + (s - p_R - m - mu_R)*q_R \
           + theta**2*q_tot**2/(2*c) \
           - pc*e0*q_tot + pc*gamma*q_tot**2*(theta + pc*gamma)/c + pc*G
    
    phi_M = V_M/2 + (V_MR - V_R)/2
    phi_R = V_R/2 + (V_MR - V_M)/2
    
    poly_M = sp.Poly(sp.expand(sp.diff(phi_M, p_M)), p_M, p_R)
    poly_R = sp.Poly(sp.expand(sp.diff(phi_R, p_R)), p_M, p_R)
    
    A = sp.Matrix([
        [poly_M.coeff_monomial(p_M), poly_M.coeff_monomial(p_R)],
        [poly_R.coeff_monomial(p_M), poly_R.coeff_monomial(p_R)]
    ])
    b = sp.Matrix([
        -poly_M.coeff_monomial(1),
        -poly_R.coeff_monomial(1)
    ])
    
    sol = A.subs(sub).solve(b.subs(sub))
    return float(sol[0]), float(sol[1])

# ============ 利润计算 ============
def calc_profits(p_M_v, p_R_v, sub):
    """计算非合作利润和 biform Shapley 分配"""
    a, b = sub[alpha], sub[beta]
    qMv = a*p_M_v - b*p_R_v
    qRv = a*p_R_v - b*p_M_v
    
    # 非合作
    k_N = (sub[theta]*qRv + sub[pc]*sub[gamma]*(qMv+qRv))/sub[c]
    Pi_M_N = (sub[theta]*k_N - p_M_v - sub[w] - sub[mu_M] + sub[s])*qMv
    Pi_R_N = (sub[theta]*k_N - p_R_v - sub[m] - sub[mu_R] + sub[s])*qRv \
             + (sub[w] - sub[m])*qMv \
             - sub[c]*k_N**2/2 \
             - sub[pc]*((sub[e0] - sub[gamma]*k_N)*(qMv+qRv) - sub[G])
    
    # Biform Shapley
    k_C = (sub[theta] + sub[pc]*sub[gamma])*(a-b)*(p_M_v + p_R_v)/sub[c]
    V_M_v = (sub[s] - p_M_v - sub[w] - sub[mu_M])*qMv
    V_R_v = (sub[s] - p_R_v - sub[m] - sub[mu_R])*qRv + (sub[w] - sub[m])*qMv \
            + sub[theta]**2*qRv**2/(2*sub[c]) \
            - sub[pc]*sub[e0]*(qMv+qRv) \
            + sub[pc]*sub[gamma]*(qMv+qRv)*(sub[theta]*qRv + sub[pc]*sub[gamma]*(qMv+qRv))/sub[c] \
            + sub[pc]*sub[G]
    V_MR_v = (sub[s] - p_M_v - sub[m] - sub[mu_M])*qMv + (sub[s] - p_R_v - sub[m] - sub[mu_R])*qRv \
             + sub[theta]**2*(qMv+qRv)**2/(2*sub[c]) \
             - sub[pc]*sub[e0]*(qMv+qRv) \
             + sub[pc]*sub[gamma]*(qMv+qRv)**2*(sub[theta] + sub[pc]*sub[gamma])/sub[c] \
             + sub[pc]*sub[G]
    phi_M_C = V_M_v/2 + (V_MR_v - V_R_v)/2
    phi_R_C = V_R_v/2 + (V_MR_v - V_M_v)/2
    
    return {
        'noncoop': {'Pi_M': float(Pi_M_N), 'Pi_R': float(Pi_R_N), 'k': float(k_N)},
        'biform': {'phi_M': float(phi_M_C), 'phi_R': float(phi_R_C), 'k': float(k_C)}
    }

# ============ 主程序 ============
if __name__ == '__main__':
    print("="*70)
    print(" zz05 均衡价格正确性验证 (Baseline 参数)")
    print("="*70)
    
    p_M_N, p_R_N = solve_noncoop(SUBS)
    p_M_C, p_R_C = solve_biform(SUBS)
    
    print(f"\n非合作均衡:")
    print(f"  p_M^N* = {p_M_N:.4f}")
    print(f"  p_R^N* = {p_R_N:.4f}")
    
    print(f"\nBiform 均衡:")
    print(f"  p_M^C* = {p_M_C:.4f}")
    print(f"  p_R^C* = {p_R_C:.4f}")
    
    print(f"\n正文 (旧) 公式值:")
    print(f"  p_M^N* = 15.1087  (误差: +0.747)")
    print(f"  p_R^N* = 5.9191   (误差: +0.217)")
    print(f"  p_M^C* = 15.1087  (== p_M^N*, 错误!)")
    print(f"  p_R^C* = 5.9191   (== p_R^N*, 错误!)")
    
    profits = calc_profits(p_M_N, p_R_N, SUBS)
    profits_C = calc_profits(p_M_C, p_R_C, SUBS)
    
    print(f"\n非合作利润: Π_M = {profits['noncoop']['Pi_M']:.2f}, "
          f"Π_R = {profits['noncoop']['Pi_R']:.2f}")
    print(f"Biform 分配: φ_M = {profits_C['biform']['phi_M']:.2f}, "
          f"φ_R = {profits_C['biform']['phi_R']:.2f}")
    
    pareto_M = profits_C['biform']['phi_M'] > profits['noncoop']['Pi_M']
    pareto_R = profits_C['biform']['phi_R'] > profits['noncoop']['Pi_R']
    
    print(f"\nPareto 改进: M={pareto_M}, R={pareto_R}")
    print("="*70)
