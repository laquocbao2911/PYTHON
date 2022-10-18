from sympy import *
import numpy as np

a=np.array([[2,-4,4,0.077],[0,-2,2,-0.056],[2,-2,0,0]])
b=np.array([3.86,-3.47,0]).T

print(np.linalg.solve(a,b))
