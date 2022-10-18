import numpy as np

a1 = np.array([[1,-7],[-2,-3]])
print("A1) L1 = "+str(max(np.sum(abs(a1),axis=0))))

a2 = np.array([[-2,8],[3,1]])
print("A2) L1 = "+str(max(np.sum(abs(a2),axis=0))))

a3 = np.array([[2,-8],[3,1]])
print("A3) L1 = "+str(max(np.sum(abs(a3),axis=0))))

a4 = np.array([[2,3],[1,-1]])
print("A4) L1 = "+str(max(np.sum(abs(a4),axis=0))))

a5 = np.array([[5,-4,2],[-1,2,3],[-2,1,0]])
print("A5) L1 = "+str(max(np.sum(abs(a5),axis=0))))