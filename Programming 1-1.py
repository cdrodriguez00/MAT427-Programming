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

taylortest = [1] #testing
taylorndegreetest = [5] #testing
'''
x is where the expansion will be calculated at
a is the center of the expansion = defaulted at 0 so not necessary
n is the number of terms calculated in the taylor's polynomial
'''

def taylor1(x=taylorx, n=taylorndegree):
    results = []
    for x in taylorx:
        for n in taylorndegree:
            taylorcalc = 0 #taylor calculation originally set to 0
            for i in range(n + 1):
                taylorcalc += (-x)**i / (math.factorial(i))
            results.append((x, n, taylorcalc)) # adds each taylor term calculated for the x and n to its own result
    return results

print(taylor1())
'''
Relative error = abs(A - An) / abs(A)

approxnege = taylor1(x,n)
exactnege = math.exp(-x)

'''

def taylor2(x=taylorx, n=taylorndegree):
    results = []
    for x in taylorx:
        for n in taylorndegree:
            taylorcalc = 0
            for i in range(n+1):
                taylorcalc += 1 / ((-x)**i / (math.factorial(1)))
            results.append((x, n, taylorcalc))
    return results

print(taylor2())


