import matplotlib.pyplot as plt
import numpy as np
import tkinter


def NFF(x, y, n):
    global xx, f
    z = y
    xx = np.linspace(0, 2, 100)
    f = []
    for ii in range(len(xx)):
        y = z
        p = y[0]
        a = []
        h = x[1] - x[0]
        s0 = (xx[ii] - x[0]) / h
        s = 1
        a.append(y[0])
        for i in range(n-1):
            delf = []
            for j in range(n-1-i):
                delf.append(y[j+1] - y[j])
            s = s*(s0-i)/(i+1)
            p = p+s*delf[0]
            y = delf
            a.append(y[0])
        f.append(p)


n = 5
x = [0, 0.5, 1, 1.5, 2]
y = [0, 1, 0, -1, 0]
NFF(x, y, n)

plt.plot(xx, f)
plt.plot(x, y, 'X')
plt.show()
