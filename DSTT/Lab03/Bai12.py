import numpy as np
import random

a = np.array([[6,0,0,5],[1,7,2,-5],[2,0,0,0],[8,3,1,8]])
b = np.array([1,-2,5,2,0,0,3,0,2,-6,-7,5,5,0,4,4]).reshape(4,4)
c = np.array([3,5,-8,4,0,-2,3,-7,0,0,1,5,0,0,0,2]).reshape(4,4)
d = np.array([4,0,0,0,7,-1,0,0,2,6,3,0,5,-8,3,0,5,-8,4,-3]).reshape(4,5)
e = np.array([[4,0,-7,3,-5],[0,0,2,0,0],[7,3,-6,4,-8],[5,0,5,2,-3],[0,0,9,-1,2]])
f = np.array([[6,3,2,4,0],[9,0,-4,1,0],[8,-5,6,7,1],[3,0,0,0,0],[4,2,3,2,0]])

print("A = "+str(np.linalg.det(a)))
print("B = "+str(np.linalg.det(b)))
print("C = "+str(np.linalg.det(c)))
# print("D = "+str(np.linalg.det(d)))
print("E = "+str(np.linalg.det(e)))
print("F = "+str(np.linalg.det(f)))