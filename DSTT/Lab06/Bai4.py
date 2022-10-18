import numpy as np
import math

u = np.array([1,1])
v = np.array([0,1])
a = math.acos(sum(u*v)/(np.linalg.norm(u,2)*np.linalg.norm(v,2)))
print("a) = "+str(a))

u = np.array([1,0])
v = np.array([0,1])
b = math.acos(sum(u*v)/(np.linalg.norm(u,2)*np.linalg.norm(v,2)))
print("b) = "+str(b))

u = np.array([-2,3])
v = np.array([1/2,-1/2])
c = math.acos(sum(u*v)/(np.linalg.norm(u,2)*np.linalg.norm(v,2)))
print("c) = "+str(c))