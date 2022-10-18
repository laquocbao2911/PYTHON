import numpy as np

def is_linear_combination(M):
    Z = [0]*len(M)
    print("Z = "+str(Z))
    if len(M[0]) != len(M[1]):
        giatri = np.linalg.solve(M,np.array(Z))
        if len(giatri[giatri!=0])==0:
            print("linearly independent")
        else:
            print("linearly dependent")
    else:
        if(np.linalg.det(M)==0):
            print("not linearly independent")
        else:
            print("linearly independent")
            print(np.linalg.solve(M,np.array(Z)))

M1 = np.array([[1,0,1],[-2,-4,-1],[0,1,1]])
print(is_linear_combination(M1))
M2 = np.array([[1,0,2],[0,1,-2],[2,4,-4]])
print(is_linear_combination(M2))
M3 = np.array([[0, 0, 1, 2, 3],
               [0, 0, 2, 3, 1],
               [1, 2, 3, 4, 5],
               [2, 1, 0, 0, 0],
               [-1, -3, -5, 0, 0]])
print(is_linear_combination(M3))