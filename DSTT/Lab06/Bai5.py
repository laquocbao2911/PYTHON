import numpy as np
import math

u = np.array([2,3])
a = u/np.linalg.norm(u,2)
print("a) = "+str(a))

u = np.array([1,2,3])
b = u/np.linalg.norm(u,2)
print("b) = "+str(b))

u = np.array([1/2,-1/2,1/4])
c = u/np.linalg.norm(u,2)
print("c) = "+str(c))

u = np.array([math.sqrt(2),2,-math.sprt(2),])
d = u/np.linalg.norm(u,2)
print("d) = "+str(d))