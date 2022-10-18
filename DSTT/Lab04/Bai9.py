import numpy as np
from sympy import *

x,y,z=symbols('x,y,z')

a = np.array([[0.61, 0.29, 0.15], [0.35, 0.59, 0.063], [0.04, 0.12, 0.787]])
b = np.array([x,y,z])

print(np.linalg.inv(a)@b)