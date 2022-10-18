import numpy as np
import math

lst = [chr(i) for i in range(65,91)]
lst.append(" ")
E = np.array([[80,98,99,85,106,94],[71,92,76,95,100,92],[124,163,140,160,176,161]])
A = np.array([[1,2,3],[2,1,2],[3,2,4]])
k = 3
temp = np.linalg.inv(A)
D2 = np.dot(temp,E).T
D1 = D2 - k - 1
D1 = np.round(D1).astype(int)
result = ""
for i in range(0,len(D1)):
    for j in range(0,len(D1[0])):
        result += lst[D1[i][j]]
print(result)