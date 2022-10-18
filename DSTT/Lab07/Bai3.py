import numpy as np

def cau3(matran):
    temp = 0
    if len(matran) == len(matran[0]):
        temp = matran*matran.T
        temp2 = np.eye(len(matran))
        result = temp - temp2
        if result.all() == 0:
            return "true"
        else:
            return "false"
    return "false"
matran = np.array([[3,1,1],[-1,2,1],[-1/2,2,7/2]])
print(cau3(matran))