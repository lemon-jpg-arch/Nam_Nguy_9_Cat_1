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

    height = f(x_sample)
    area = height * dx
    total_area += area

    print(f"Rect {i+1}: interval [{left:.3f}, {right:.3f}] "
          f"sample x = {x_sample:.3f} "
          f"height f(x) = {height:.3f} "
          f"area = {area:.3f}")

print("="*50)
print(f"Total estimated area = {total_area:.3f}")
print("="*50)

# Plotting
x_vals = np.linspace(lowerB, upperB, 200)
y_vals = [f(x) for x in x_vals]

plt.figure()
plt.plot(x_vals, y_vals, label=f"f(x) = {func}")

# Draws rectangles
for i in range(numRect):
    left = lowerB + i * dx
    right = left + dx

    if method == "L":
        x_sample = left
        align = 'edge'
    elif method == "R":
        x_sample = right
        align = 'edge'
        left = right - dx
    else:  # Midpoint
        x_sample = (left + right) / 2
        align = 'center'

    plt.bar(left if align == 'edge' else x_sample,
            f(x_sample),
            width=dx,
            align=align,
            alpha=0.3,
            edgecolor='black')

plt.title(f"Area Estimate ({method} rectangles) = {total_area:.3f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.show()