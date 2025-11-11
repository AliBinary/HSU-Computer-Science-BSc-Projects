# AliGhanbari
# student number: 4001239216
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(0, np.pi/2, 25)

ax1 = plt.subplot(221)
ax1.plot(x, np.sin(x), 'r-o')
ax1.set_title('y=sin(x)')

ax2 = plt.subplot(222)
ax2.plot(x, 1/np.tan(x), 'b-^')
ax2.set_title('y=cot(x)')

ax3 = plt.subplot(212)
ax3.plot(x, x+2, 'g-s')
ax3.set_title('y=x+2')

plt.show()
