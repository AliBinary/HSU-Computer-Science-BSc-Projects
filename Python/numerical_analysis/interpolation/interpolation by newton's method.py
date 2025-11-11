import numpy as np


def newton_interpolation(x, y, xp):
    n = len(x)
    a = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1])/(x[i] - x[i-j])
    yp = a[n-1]
    for i in range(n-2, -1, -1):
        yp = a[i] + (xp - x[i])*yp
    return yp


# Example usage
x = np.array([1, 2, 3])
# x = np.array(input("Enter the x values separated by spaces: ").split(), dtype=float)
y = np.array([4, 5, 6])
# y = np.array(input("Enter the y values separated by spaces: ").split(), dtype=float)
xp = 2.5
# xp = float(input("Enter the value to be interpolated: "))
yp = newton_interpolation(x, y, xp)
print(f"Interpolated value at {xp} is {yp}")
