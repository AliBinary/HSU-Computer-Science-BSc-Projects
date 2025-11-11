n = int(input("enter n: "))
r = int(input("enter r: "))
s = i = 0
while n > 0:
    R = n % r
    s = s + R * 10**i
    n = n // r
    i += 1
print(s)
