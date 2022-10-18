import numpy as np
import math

q = np.array([0, 0, 0.7, 0.5, 0, 0.3])
matran = np.array([[1, 0.5, 0.3, 0, 0, 0],
                 [0.5, 1, 0, 0, 0, 0],
                 [0, 1, 0.8, 0.7, 0, 0],
                 [0, 0.9, 1, 0.5, 0, 0],
                 [0, 0, 0, 1.0, 0, 1.0],
                 [0, 0, 0, 0, 0.7, 0],
                 [0.5, 0, 0.7, 0, 0, 0.9],
                 [0, 0.6, 0, 1, 0.3, 0.2]])

max = np.dot(q, matran[0])/(np.linalg.norm(q)*np.linalg.norm(matran[0]))
check = 0
for i in range(len(matran)):
    cosin = np.dot(q, matran[i])/(np.linalg.norm(q)*np.linalg.norm(matran[i]))
    if max < cosin:
        max = cosin
        check = i

print("D{} with cos_sim = {}".format(check+1,max))