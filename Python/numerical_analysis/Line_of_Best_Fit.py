import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# read excel file
df = pd.read_excel('numerical_analysis\\file.xlsx')

# extract x and y coordinates from the dataframe
x = df['x']
y = df['y']
print(f"\nYou have entered {len(x)} points in the Excel file.\n")

# fit a line to the points using numpy's polyfit function
m, b = np.polyfit(x, y, 1)

# create figure and axis objects
fig, ax = plt.subplots()
plt.title("Line of Best Fit")

# create empty line object
line, = ax.plot([], [], lw=2)

# plot the points
points, = ax.plot(x, y, 'ro')


def init():  # initialization function
    # creating an empty plot/frame
    line.set_data([], [])
    return line,


# X, Y values to be plotted
min_value = min(x)
max_value = max(x)
x = list(np.linspace(min_value, max_value, 100))
y = [m*i+b for i in x]


def animate(i):  # animation function
    # appending new values to x and y axes points list
    line.set_data(x[:i], y[:i])
    return line,


# call the animator
anim = FuncAnimation(fig, animate, init_func=init, frames=1000, interval=20)

# show the plot
ax.legend(['fit line', 'points'])
plt.show()
