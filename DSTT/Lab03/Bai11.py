import numpy as np
import random

A = np.array([[2,4,1],[6,7,2],[3,5,9]])

print("Câu a")
print("A is matrix square") if len(A)==len(A[0]) else print("A is not matrix square")

print("Câu b")
b = A - np.transpose(A)
if len(A)==len(A[0]) and np.all(b==0):
    print("A is matrix symmetric") 
else:
    print("A is not matrix symmetric")

print("Câu c")
if len(A)==len(A[0]) and np.all(A == -np.transpose(A)):
    print("A is matrix skew-symmetric")
else: 
    print("A is not matrix skew-symmetric")

D = A.copy()
print("Câu d")
for i in range(0,len(D)):
    for j in range(0,len(D[i])):
        if i>0 and j<i:
            D[i][j] = 0
print(D)

E = A.copy()
print("Câu e")
for i in range(0,len(E)):
    for j in range(0,len(E[i])):
        if j>i:
            E[i][j]=0
print(E)