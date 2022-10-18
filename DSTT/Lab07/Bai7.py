from sympy import * 
import numpy as np
A = Matrix([[1 ,0, 2, 3],[4,-1, 0, 2],[0,-1 ,-8, -10]])
a,b=symbols('a,b')

M = A.nullspace()
v1,v2= M[0],M[1]
temp1 = list(v1)
temp2 = list(v2)
M_null = [temp1,temp2]
print(M_null)

result = A.T*Matrix([[a*v1[0]-b*v2[0]],[a*v1[1]-b*v2[1]],[a*v1[2]-b*v2[2]]])
print(result)
