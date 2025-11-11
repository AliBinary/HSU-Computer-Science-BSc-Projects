# AliGhanbari
# student numer: 4001239216
import numpy as np

# الف
A = np.array([[0, 0, 1],
              [2, 3, 9],
              [2, 1, 6]])

print("my matrix")
print(A)

det = np.linalg.det(A)
print("\ndet :", det)

print("\ninverse of my matrix: ")
B = (1/det) * A
print(B)

# ب
sum = 0
for i in range(3):
    sum += A[i][i]

print("the main diameter of my matrix: ", sum)
