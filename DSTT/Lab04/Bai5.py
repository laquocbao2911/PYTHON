from sympy import *
import numpy as np

a=np.array([[1,2,1], [2,2,2], [2,4,1]])
b=np.array([1,1,2])

print(np.linalg.solve(a,b.T))
