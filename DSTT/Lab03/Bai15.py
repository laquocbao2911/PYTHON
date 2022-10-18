import numpy as np
import random

arrayA = np.array([[2,4,5/2],[-3/4,2,1/4],[1/4,1/2,2]])
arrayB = np.array([[1,-1/2,3/4],[3/2,1/2,-2],[1/4,1,1/2]])

a1 = np.linalg.inv(arrayA)*np.linalg.inv(arrayB)
a2 = np.linalg.inv(arrayA*arrayB)
a3 = np.linalg.inv(arrayB*arrayA)
b1 = np.transpose(np.linalg.inv(arrayA))
b2 = np.linalg.inv(np.transpose(arrayA))

print("(A^-1)x(B^-1) = "+str(a1))
print("(AxB)^-1 = "+str(a2))
print("(BxA)^-1 = "+str(a3))
print("(A^-1)^T = "+str(b1))
print("(A^T)^-1 = "+str(b2))