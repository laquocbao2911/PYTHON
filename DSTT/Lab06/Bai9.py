import numpy as np
import math
matran = np.array([[0,4,0,0,0,2,1,3], 
              [3,1,4,3,1,2,0,1], 
              [3,0,0,0,3,0,3,0],
              [0,1,0,3,0,0,2,0],
              [2,2,2,3,1,4,0,2]])
temp = 0
for i in range(len(matran)-1):
    for j in range(i+1,len(matran)):
        temp = np.dot(matran[i], matran[j])/(np.linalg.norm(matran[i],2)*np.linalg.norm(matran[j],2))
        print("Doc {}, Doc {}, cosin = {}".format(i+1,j+1,temp))
