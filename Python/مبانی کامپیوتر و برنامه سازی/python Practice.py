# Ali Ghanbari--- student number: 4001239216
# الف
def factorial(x):
    Y, s = (1, 1)
    while Y <= x:
        s = s * Y
        Y += 1
    return int(s)


# ب
def combination(p, o):
    output = factorial(p) / (factorial(p - o) * factorial(o))
    return int(output)


print(factorial(int(input('enter n for factorial: '))))
print("""------------------------------
#COMBINATION k form n""")
k = int(input('first enter k for combination: '))
n = int(input('now enter n for combination: '))
print(combination(n, k))


print('------------------------------')
# ج
n = int(input("enter n for Khayyam Triangle! :"))
i, j = (0, 0)
while j <= n:
    space = 0
    while space <= n-j:
        print(end=' ')
        space += 1
    while i <= j:
        m, k = (j, 0)
        while k <= j:
            print(combination(m, k), end=' ')
            k += 1
        i += 1
    print('')
    j += 1
