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
            taylor_calc = 0 #taylor calculation originally set to 0
            for i in range(n+1):
                taylor_calc += (-x)**i / (math.factorial(i))

            actual_nege = math.exp(-x)  # actual e^-x

            if actual_nege == 0 or (actual_nege) < 1e-500:
                relative_error = float("inf")
            else:
                relative_error = relative_error = abs(taylor_calc - actual_nege) / abs(actual_nege)
            results.append((x, n, relative_error))  # adds each taylor term calculated for the x and n to its own result
    return results

print(taylor1())
'''
Relative error = abs(A - An) / abs(An)

approxnege = taylor1(x,n)
exactnege = math.exp(-x)

'''
print(" ")
print(" ")
def taylor2(x=taylorx, n=taylorndegree):
    results = []   # create empty result list
    for x in taylorx:    # iterates through my x and n lists
        for n in taylorndegree:
            taylorcalc = 0
            for i in range(n+1):
                taylorcalc += x**i / (math.factorial(i))   # calculates each taylor term and sums to the taylorcalc variable for each x and n

            actual_nege = math.exp(-x)  #actual e^-x

            if taylorcalc == 0: # for error
                taylor_reciprical = float("inf")
            else:
                taylor_reciprical = 1 / taylorcalc

            if actual_nege == 0 or abs(actual_nege) < 1e-500:     # more error
                relative_error = float("inf")
            else:
                relative_error = relative_error = abs(taylor_reciprical - actual_nege) / abs(actual_nege)

            results.append((x, n, relative_error))  # adds numbers and result to results list
    return results

print(taylor2())


"""
Results Discussion:
Function 1
As n increases for a positive x, the error decreases accurately for large n, for small x. For large x, the error becomes 
extremely large for small n and gets catastrophically bad for large n. This can demonstrate the compounding errors from 
subtracting large numbers. This gets so large that there are inf errors. For "small" x that are negative, we get errors
that are small for small and large n. As our x increases, we do not get consistent bounds for error where there is no 
clear direction in increasing or decreasing error.


Function 2




"""