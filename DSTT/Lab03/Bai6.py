import numpy as np
import random

A = np.array([2,4,1,6,7,2,3,5,9]).reshape(3,3)
x1 = A[0,:]
print("x1 = "+str(x1))
Y = A[len(A)-2:,:]
print("Y = "+str(Y))