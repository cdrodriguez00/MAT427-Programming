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

def exact_polynomial(x):
    return (x-2) ** 9

def standard_polynomial(p, x):
    result = 0
    power = 1
    for i in range(len(p)):
        result += p[i] * power
        power *= x
    return result


"""
2
"""
def horner(p,x):
    N = len(p)-1
    p_x = p(N)

    for k in range(N-1, -1, -1):
        p_x = p[k] + p_x * x

    return p_x

def domain(a, b, N):
    h = (b-a) / N  ### defined h with N as an integer on the interval [a,b]
    domain_x = []
    polynomial_output = []

    for k in range(N+1):
        x_k = a + k * h
        domain_x.append(x_k)
        px = standard_polynomial(p, x_k)
        polynomial_output.append(px)

def maximum_error(p, a, b, N, method):
    domain_x = domain(a,b, N)

    error = []

    for x in domain_x:
        exact_value = exact_polynomial(x)
        approximate_value = method(p,x)
        error.append(abs(exact_value-approximate_value))

    return max(error)

"""
3
"""
p = [-512, 2304, -4608, 5376, -4032, 2016, -672, 144, -18, 1]
a = 1.92
b = 2.08
N = 1000

standard_polynomial_error = maximum_error(p,a,b,N, standard_polynomial)
horner_polynomial_error = maximum_error(p, a, b, N, horner)

print("N = ", N)
print("1. The maximum error for the standard evaluation function is", standard_polynomial_error)
print("2. The maximum error for the Horner's evaluation function is", horner_polynomial_error)







