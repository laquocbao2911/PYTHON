from sympy import *
import numpy as np

a1 = np.array([[1,2,1],[2,-1,1],[2,1,0]])
b1 = np.array([0,0,0])
caua = np.linalg.solve(a1,b1.T)
print(caua)

a2 = np.array([[2,1,1,1],[1,2,1,1],[1,1,2,2],[1,1,1,2]])
b2 = np.array([1,1,1,1])
caub = np.linalg.solve(a2,b2.T)
print(caub)