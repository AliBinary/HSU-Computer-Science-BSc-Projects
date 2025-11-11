import numpy as np


def _poly_newton_coefficient(x, f):
    m = len(x)

    x = np.copy(x)
    a = np.copy(f)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])

    return a


def newton_polynomial(x_data, f_data, x):
    a = _poly_newton_coefficient(x_data, f_data)
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p


n = int(input("Enter number of data points: "))
print("Enter data for x and f:")

x = []
f = []
for i in range(n):
    x.append(float(input('x['+str(i)+']=')))
    f.append(float(input('f['+str(i)+']=')))

xp = float(input('Enter interpolation point: '))

print(newton_polynomial(x, f, xp))
