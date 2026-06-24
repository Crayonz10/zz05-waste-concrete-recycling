#!/usr/bin/env python3
"""Check actual carbon emissions vs quota"""
import numpy as np

ALPHA = 1.5
BETA = 0.134
M = 32
W = 35
S = 87.5
MIU_M = 25
MIU_R = 44
C = 135000
THETA = 137.5
PC_VAL = 65
E_VAL = 0.035


def calc_biform(a, b, th, c, s, w, m, mM, mR, pc, e, G):
    den = (a-b)**3*(a+b)*th**4 - 4*c*(a-b)*(3*a*a-b*b)*th*th + 4*c*c*(4*a*a-b*b)
    if abs(den) < 1e-10: den = 1e-10
    num_pM = 4*c*c*(2*a*a*(s-w-mM)+a*b*(s-m-mR)-b*b*(w-m)) - 2*c*th*th*((a-b)*(a*a*(s-w-mM)-(a*a-a*b+b*b)*(w-m))-a*(a*a-a*b+b*b)*(mM-mR)) - 4*c*a*pc*e*(a-b)*(a*a-a*b+b*b)
    pM = num_pM / den
    num_pR = 4*c*c*a*(2*a*(s-m-mR)+b*(s-3*w+2*m-mM)) - 2*c*a*th*th*((a-b)*(a*(w-m)+b*(s-3*w+2*m-mM))+a*(a-2*b)*(mM-mR)) - 4*c*pc*e*(a-b)*(c*(2*a*a-b*b)-th*th*a*(a-b))
    pR = num_pR / den
    qM = a*pM - b*pR
    qR = a*pR - b*pM
    q_total = qM + qR
    carbon_emissions = e * q_total
    return carbon_emissions


if __name__ == '__main__':
    a, b, th, c, s, w, m, mM, mR = ALPHA, BETA, THETA, C, S, W, M, MIU_M, MIU_R
    pc, e = PC_VAL, E_VAL

    carbon_emissions = calc_biform(a, b, th, c, s, w, m, mM, mR, pc, e, 300)
    print(f"Carbon emissions from recycling: {carbon_emissions:.2f} tons")
    print(f"Carbon quota G range in paper: 100-500 tons")
    print(f"Baseline G in paper: 300 tons")
    print(f"\n=> Emissions {carbon_emissions:.1f} < G=300, so no carbon purchase needed!")
    print(f"Need to increase e or decrease G to see effect")