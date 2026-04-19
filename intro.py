from math import *
import matplotlib.pyplot as plt
import numpy as np

# Asks for user inputs
func = input("Enter a function in terms of x (e.g. x2, x^3 + 2, sin(x)): ")
func = func.replace("^","**")
lowerB = float(input("Lower bound a = "))
upperB = float(input("Upper bound b = "))
numRect = int(input("How many rectangles? n = "))
method = input("Choose method (L=left, R=right, M=midpoint): ").upper()

# Defined function
def f(x):
    return eval(func, {"x": x, **globals()})

