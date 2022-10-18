from sympy import *
import numpy as np

a = np.array([[1, 1, 2], [3, 6, -5], [2, 4, -3]])
b = np.array([1, -1, 0]).T
det_A = np.linalg.det(a)
print(det_A)
print(" Is A invertible?", "True" if det_A != 0 else "False")
print(np.linalg.solve(a, b))
