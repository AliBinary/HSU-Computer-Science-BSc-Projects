
from math import factorial
i = 1
s = 0
n = int(input("n:"))
while i <= n:
    s = s + 1/factorial(i)
    i = i+1
print(s)
