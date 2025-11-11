from scipy.integrate import simps
import numpy as np
import scipy.integrate as spi

N = 10
a = 0
b = 1
x = np.linspace(a, b, N+1)
y = 3*x**2
appoximation = spi.simps(y, x)
print(appoximation)
