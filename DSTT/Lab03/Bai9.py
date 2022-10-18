import numpy as np
import random

T = np.array([[0.6,0.7],[0.4,0.3]])
p = np.array([0.5,0.5]).reshape(2,1)

def pk(T,p,k):
    return pow(T,k)*p

for i in (1,2,10,100,100000):
    print("p[%d] = \n"%(i) + str(pk(T,p,i)))