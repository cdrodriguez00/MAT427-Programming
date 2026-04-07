"""""
Name: Cristian Rodriguez
Class: MAT427
Date: 4/2/26
Assignment: Chapter 2.1
Horner's Method
"""

"""
1
"""
def polynomial(p, x):
    result = 0
    power = 1
    for i in range(len(p)):
        result += p[i] * power
        power *= x
    return result

def horner(p,x):
    N = len(p)-1
    p_x = p(N)

    for k in range(N-1, -1, -1):
        p_x = p[k] + p_x * x

    return p_x

def domain(p, a, b, N):
    h = (b-a) / N  ### defined h with N as an integer on the interval [a,b]
    domain_x = []
    polynomial_output = []

    for k in range(N+1):
        x_k = a + k * h
        domain_x.append(x_k)
        px = polynomial(p, x_k)
        polynomial_output.append(px)





