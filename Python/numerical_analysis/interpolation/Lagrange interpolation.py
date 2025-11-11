import numpy as np


def lagrange_interpolation(x, y, xp):
    yp = 0
    n = len(x)
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j])/(x[i] - x[j])
        yp += y[i]*p
    return yp


# Example usage
x = np.array([1, 2, 3])
# x = np.array(input("Enter the x values separated by spaces: ").split(), dtype=float)
y = np.array([4, 5, 6])
# y = np.array(input("Enter the y values separated by spaces: ").split(), dtype=float)
xp = 2.5
# xp = float(input("Enter the value to be interpolated: "))
yp = lagrange_interpolation(x, y, xp)
print(f"Interpolated value at {xp} is {yp}")
