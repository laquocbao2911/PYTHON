import numpy as np
y = np.array([7, 6])
u = np.array([4, 2])

def cau2(u,y):
    return (sum(y*u)/sum(u*u))*u
print(cau2(u,y))