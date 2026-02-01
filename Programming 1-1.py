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

'''
x is where the expansion will be calculated at
a is the center of the expansion = defaulted at 0
n is the number of terms calculated in the taylor's polynomial
'''

def taylor1(x=None, a=0, n=None):
    taylor = 0
    if x is None:
        x = taylorx
    if n is None:
        n = taylorndegree
    for x in x:
        for n in n:
            taylor += x**n / (math.factorial(x))

print(taylor1())

'''
Relative error = abs(A - An) / abs(A)


approxnege = taylor1(x,n)
exactnege = math.exp(-x)

'''