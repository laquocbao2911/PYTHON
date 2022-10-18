import numpy as np

def vector(v1, v2, v3,v4,w,ind):
    if len(w)!=len(v1):
        return False
    if ind == 1:
        if np.linalg.matrix_rank(np.array([v1, v2, v3]))<np.linalg.matrix_rank(np.array([v1, v2, v3,w])):
            return False
    elif ind == 2:
        if np.linalg.matrix_rank(np.array([v1, v2, v3,v4]))<np.linalg.matrix_rank(np.array([v1, v2, v3,v4,w])):
            return False
    return True


v1 = np.array([1, 2, 3, 4])
v2 =np.array([-1, 0, 1, 3])
v3 =np.array([0, 5, -6, 8])
w =np.array([3, -6, 17, 11])

# Câu a 
print(vector(v1, v2, v3,w,1))

# Câu b
v4 =np.array([1, 15, -12, 8])
print(vector(v1, v2,v3,v4,w,2))