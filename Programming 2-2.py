"""""
Name: Cristian Rodriguez
Class: MAT427
Date: 4/2/26
Assignment: Chapter 2.2
Difference Quotients
"""

import math

def forward_diff_quotient(f, x, h):
    return (f(x+h) - f(x))/ h

def backward_diff_quotient(f, x, h):
    return (f(x) - f(x-h)) / h

def central_diff_quotient(f, x, h):
    return (f(x+h)-f(x-h)) / h

def better_foward_diff_quotient(f, x, h):
    return(f(x + 2*h) - f(x)) / 2*h

def derivative_approx (f,x, h):
    2*forward_diff_quotient(f,x,h) - better_foward_diff_quotient(f,x,h)

def convergence(errors):
    calculations = [None]

    for i in range(1, len(errors)):

        calculation = math.log(better_foward_diff_quotient() / forward_diff_quotient()) / math.log(2)
        calculations.append(calculation)

    return calculations





