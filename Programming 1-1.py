"""""
Name: Cristian Rodriguez
Class: MAT427
Date: 1/29/26
Assignment: Chapter 1
Floating Point Errors
"""

# Cancellation Errors
import math

''' compute e^-x using taylor's polynomials '''
taylorx = [1, 5, 10, 50, 100, 500, 1000, -1, -5, -10, -15, -20, -50]
taylorndegree = [1, 5, 10, 50, 100]
def taylor1(x=None, n=None):
    if x is None:
        x = taylorx
    if n is None:
        n = taylorndegree
    for x in x:
        for n in n:
            (math.factorial(x))


'''
Relative error = abs(A - An) / abs(A)


approxnege = taylor1(x,n)
exactnege = math.exp(-x)

'''