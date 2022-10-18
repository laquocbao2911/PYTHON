import numpy as np
from sympy import*
import math

C = np.array([[1,0,2,3],
              [4,-1,0,2],
              [0,-1,-8,-10]])
result,privot = Matrix(C.T).rref()
print("a) "+str(privot))
result1,privot1 = Matrix(C).rref()
print("b) "+str(privot1))
