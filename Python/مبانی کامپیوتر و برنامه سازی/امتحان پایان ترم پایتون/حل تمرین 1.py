L = [4, 0, 0, 1, 2, 3, 9, 2, 1, 6]
L1 = L
L2 = L[:]
print(L[1:4])
print(L[4:])
print(L[:4])
print(L[:])
print(L[4:4])
print(L[1:6:2])
print(L[:10])
L[0] = 1000
del L[0]
L[1:3] = [2000, 3000]
del L[3:6:2]
L.append(90)
print(L)
print(L1)
print(L2)
