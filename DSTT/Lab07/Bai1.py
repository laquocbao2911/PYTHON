import numpy as np
u = np.array([[3,1,1],[-1,2,1],[-1/2,2,7/2]])
def cau1(u):
    temp = 1
    for i in range(len(u)):
        temp *= u[i]
    tong = sum(temp)
    if tong == 0:
        return "an orthogonal set"
    else:
        return "not an orthogonal set"
print(cau1(u))