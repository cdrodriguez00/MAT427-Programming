"""""
Name: Cristian Rodriguez
Class: MAT427
Date: 4/2/26
Assignment: Chapter 2.2
Difference Quotients
"""


def right_hand_diff_quotient(f, x, h):
    return (f(x+h) - f(x))/ h

def left_hand_diff_quotient(f, x, h):
    return (f(x) - f(x-h)) / h

def central_diff_quotient(f, x, h):
    return (f(x+h)-f(x-h)) / h