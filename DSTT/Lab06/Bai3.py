import numpy as np

c1 = np.array([[5,-4,2],[-1,2,3],[-2,1,0]])
print("a) Frobenius-norm = "+str(np.sqrt(np.sum(c1**2))))

c2 = np.array([[1,7,3],[4,-2,-2],[-2,-1,1]])
print("b) Frobenius-norm = "+str(np.sqrt(np.sum(c2**2))))

c3 = np.array([[2,3],[1,-1]])
print("c) Frobenius-norm = "+str(np.sqrt(np.sum(c3**2))))