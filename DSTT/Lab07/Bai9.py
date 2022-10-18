import numpy as np
import sympy as sp
A = np.array([[5 ,1, 2, 2, 0],
              [3, 3, 2,-1, -12],
              [8, 4, 4, -5, 12],
              [2 ,1 ,1 ,0 ,-2]])
B = np.array([[5,3,8,2],
              [1,3,4,1],
              [2,-1,-5,0]])
C= A.T
print(C)
# Explain why a3 and a5 are in the column space of B
def columnSpace(C,B):
    if np.linalg.matrix_rank(B)<np.linalg.matrix_rank(np.array([C[2],C[4],B[0],B[1],B[2]])):
        return False
    return True
print(columnSpace(C,B))