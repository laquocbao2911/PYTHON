import numpy as np
import math

lst = [chr(i) for i in range(65,91)]
lst.append(" ")
mess1 = "ATTACK"
mess2 = "LINEAR ALGEBRA LABORATORY"
A = np.array([[3,4,5],[1,3,1],[1,1,2]])
k = 3

def encodeMes(A,lookupTable,k,mess):
    temp = []
    for i in mess:
        for j in range(len(lookupTable)):
            if i == lookupTable[j]:
                temp.append(j)
                if i == " ":
                    temp.append(j)
                break
    temp = np.array(temp) + k + 1
    temp = temp.reshape(int(len(temp)/3),3).T
    result = A@temp
    return result

print(encodeMes(A,lst,k,mess1))
print(encodeMes(A,lst,k,mess2))