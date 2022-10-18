import numpy as np
import random

y = np.array([[1,2,16,31,22],[2,8,12,21,23],[4,9,11,14,25],[3,6,10,16,34]])

print("Câu a")
print("x="+str(y[1][1:4:1]))

print("Câu b")
caub = []
for i in range(0,len(y)):
    caub.append(y[i][2])
print("y="+str(np.array(caub)))

print("Câu c")
print("A="+str(y[1:-1,1:-1]))

print("Câu d")
caud = []
for i in range(0,len(y)):
    caud.append(y[i][::2])
print("B="+str(np.array(caud)))

print("Câu e")
caue = []
for j in range(1,len(y)):
    for i in range(0,len(y[0])):
        if i != 1:
            caue.append(y[j][i])
    
print("C="+str(np.array(caue).reshape(3,4)))

print("Câu f")
cauf = []
for i in y:
    for j in i:
        if np.any(j > 12):
            cauf.append(j)
print("D="+str(np.array(cauf)))