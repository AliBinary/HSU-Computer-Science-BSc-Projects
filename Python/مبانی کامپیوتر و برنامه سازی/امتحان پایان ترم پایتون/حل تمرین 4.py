K = 6
L = [4, 0, 0, 1, 2, 3, 9, 2, 1, 6]

# الف
T1 = 10, 20 + 40
T2 = T1*K
print(T1, '\n', T2)

# ب
y = K*200
x = K*2 if y >= 300 and y < 350 else K*5
print(x)

# ج
for i in range(4):
    del(L[i])
print(L)

# د
print(K*3+7 % (16**2**-1)**2)
