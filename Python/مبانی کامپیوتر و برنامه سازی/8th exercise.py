# Ali Ghanbari, student number: 4001239216
# 8th exercise
def factorial(x):
    i, s = (1, 1)
    while i <= x:
        s = s * i
        i += 1
    return s


U, S = (1, 0)
n = int(input('enter n:'))
while U <= n:
    S = S + 1/factorial(U)
    U += 1
print(S)
