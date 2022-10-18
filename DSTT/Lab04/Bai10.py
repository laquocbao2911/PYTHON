import numpy as np
from sympy import *

a = np.array([[0.25,0.15,0.1], [0.4,0.15,0.2], [0.15,0.2,0.2]])
b = np.array([100,100,100])
i = np.array([[1,0,0],[0,1,0],[0,0,1]])
temp = i - a
print(np.linalg.solve(temp,b.T))