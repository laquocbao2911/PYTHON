import numpy as np
import random

print("Cau a")
x = np.array([1,2,3,4,5])
print("A="+str(x.reshape(5,1)*np.ones((5,5),dtype=int)))

print("Cau b")
b= np.array([1,2,3,4,5,6])
caub = []
for i in range(0,6):
    caub.append(b)
print("B="+str(np.array(caub)))

print("Cau c")
c = np.arange(1,31).reshape(6,5).T
print("C="+str(c))

print("Cau d")
d = np.arange(1,26).reshape(5,5)
print("D="+str(d))