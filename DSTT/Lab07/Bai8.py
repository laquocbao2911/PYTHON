import numpy as np

def columnSpace(A,w):
    temp = [w]
    for i in range(len(A)):
        temp.append(A[i])
    if len(A)!=len(w):
        return False
    if np.linalg.matrix_rank(np.array(A))<np.linalg.matrix_rank(np.array(temp)):
        return False
    return True 


def checkNullSpace(A,w):
    if len(A)!=len(w):
        return False
    if np.sum(np.array(A)*np.array(w))==0:
        return True
    return False

def xulycau8(A,w):
    if columnSpace(A,w) and checkNullSpace(A,w):
        print("w is the null space and the column space.")
    elif columnSpace(A,w) and not checkNullSpace(A,w):
        print("w is the column space.")
    elif not columnSpace(A,w) and checkNullSpace(A,w):
        print("w is the null space.")
    else:
        print("w is not The null space and the column space.")

# Câu a
A1=np.array([[7, 6, -4, 1],
            [-5 ,-1 ,0 ,-2],
            [9, -11, 7, -3],
            [19 ,-9 ,7 ,1]])
w1=[1,1,-1,-3]
xulycau8(A1,w1)

A2=np.array([[-8, 5, -2, 0],
            [-5, 2, 1, -2],
            [10, -8, 6,-3],
            [3, -2, 1, 0]])
w2=[1,2,1,0]
xulycau8(A2,w2)