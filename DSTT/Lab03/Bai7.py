import numpy as np
import random

B = []
A = np.array([2,7,9,7,3,1,5,6,8,1,2,5])
for i in range(0,len(A)):
        if i%2==1:
            B.append(A[i])
print("B = "+str(np.array(B).reshape(3,int(len(B)/3))))

C = []
for i in range(0,len(A)):
        if i%2==0:
            C.append(A[i])
print("C = "+str(np.array(C).reshape(3,int(len(C)/3))))

print("new A = "+str(A.reshape(4,3)))