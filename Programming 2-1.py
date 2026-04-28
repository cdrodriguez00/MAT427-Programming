"""""
Name: Cristian Rodriguez
Class: MAT427
Date: 4/2/26
Assignment: Chapter 2.1
Horner's Method
"""

p = [-512, 2304, -4608, 5376, -4032, 2016, -672, 144, -18, 1]
a = 1.92
b = 2.08
N = 1000

def exact_polynomial(x):
    return (x-2) ** 9

"""
1
"""
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
    n = len(p)-1
    p_x = p[n]

    for k in range(n-1, -1, -1):
        p_x = p[k] + p_x * x

    return p_x

def domain(a, b, N):
    h = (b-a) / N  ### defined h with N as an integer on the interval [a,b]
    domain_x = []
    numbers = []

    for k in range(N+1):
        x_k = a + k * h
        domain_x.append(x_k)

        polynomial_calc = standard_polynomial(p, x_k)
        numbers.append(polynomial_calc)

    return domain_x


def maximum_error(p, a, b, N, method):
    domain_x = domain(a, b, N)

    error = []

    for x in domain_x:
        exact_value = exact_polynomial(x)
        approximate_value = method(p, x)
        error.append(abs(exact_value-approximate_value))

    return max(error)

"""
3
"""

standard_polynomial_error = maximum_error(p, a, b, N, standard_polynomial)
horner_polynomial_error = maximum_error(p, a, b, N, horner)

print("1. The maximum error using N=1000 for the standard evaluation function is", standard_polynomial_error)
print("2. The maximum error using N =1000 for the Horner's evaluation function is", horner_polynomial_error)







