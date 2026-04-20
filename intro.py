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

# Setup
dx = (upperB - lowerB) / numRect
total_area = 0

print("\n" + "="*50)
print(f"Rectangle Method: {method}")
print("="*50)

# Rectangle calculation
for i in range(numRect):
    left = lowerB + i * dx
    right = left + dx

    # Differentiates sample points
    if method == "L":
        x_sample = left
    elif method == "R":
        x_sample = right
        align = 'edge'
    elif method == "M":
        x_sample = (left + right) / 2
    else:
        print("Invalid method. Use L, R, or M.")
        break