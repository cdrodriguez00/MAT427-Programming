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
def taylor1(x, n):
    xvals = [-50, -20, -15, 10, -5, -1, 1, 5,10, 50, 100, 500, 1000]
    ndegree = [1, 5, 10, 50, 100]
    taylor = 1 +



'''
Relative error = abs(A - An) / abs(A)
'''

approxnege = taylor1(x,n)
exactnege = math.exp(-x)