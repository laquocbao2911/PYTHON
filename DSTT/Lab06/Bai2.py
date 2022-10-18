import numpy as np

b1 = np.array([1,-7,-2,-3])
print("B1) Loo = "+str(max(np.sum(abs(b1),axis=1))))

b2 = np.array([3,6,1,0])
print("B2) Loo = "+str(max(np.sum(abs(b2),axis=1))))

b3 = np.array([5,-4,2,-1,2,3,-2,1,0])
print("B3) Loo = "+str(max(np.sum(abs(b3),axis=1))))

b4 = np.array([3,6,-1,3,1,0,2,4,-7])
print("B4) Loo = "+str(max(np.sum(abs(b4),axis=1))))

b5 = np.array([-3,0,0,0,4,0,0,0,2])
print("B5) Loo = "+str(max(np.sum(abs(b5),axis=1))))