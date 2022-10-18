import numpy as np
import random

def dinhthuc(n):
    arrayA = np.random.randint(1,50,size=(n,n))
    arrayB = np.random.randint(1,50,size=(n,n))
    if np.linalg.det(arrayA + arrayB) == np.linalg.det(arrayA) + np.linalg.det(arrayB):
        print('true')
    else:
        print('false')

for i in range(0,3):
    n = int(input("Enter n(%d): "%(i+1)))
    dinhthuc(n)