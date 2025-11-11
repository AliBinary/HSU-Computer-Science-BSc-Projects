from turtle import *

setup(width=700, height=700)
speed("fastest")
colors = ['green', 'yellow', 'red']

G = 0.5
L = 10
left(90)

for k in range(29):
    pensize(G)
    G += 0.5
    color(colors[k % 3])
    forward(L)
    L += 10
    left(90)

color("black")

done()
