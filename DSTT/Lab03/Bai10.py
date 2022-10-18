import numpy as np
import random

A = np.array([-1,4,8,-9,1,2]).reshape(2,3)
B = np.array([5,8,0,-6,5,6]).reshape(3,2)
C = np.array([-4,1,6,5]).reshape(2,2)
D = np.array([-6,3,1,8,9,-2,6,-1,5]).reshape(3,3)

print("Câu a")
print(A*np.transpose(B))

print("Câu b")
print(B*np.transpose(C))

print("Câu c")
print(C - np.transpose(C))

print("Câu d")
print(D - np.transpose(D))

print("Câu e")
print(D)

print("Câu f")
print(2*np.transpose(C))

print("Câu g")
print(np.transpose(A) + B)

print("Câu h")
print(np.transpose(np.transpose(A) + B))

print("Câu i")
print(np.transpose(2*np.transpose(A) - 5*B))

print("Câu j")
print(np.transpose(-D))

print("Câu k")
print(-np.transpose(D))

print("Câu l")
print(np.transpose(pow(C,2)))

print("Câu m")
print(pow(np.transpose(C),2))