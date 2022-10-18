from sympy import *
import numpy as np

a=np.array([[3,3.2],[3.5,3.6]])
b=np.array([118.4,135.2]).T

print(np.linalg.solve(a,b))