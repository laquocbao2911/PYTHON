import numpy as np
import random

arr = np.array([1,2,3,4,5,6,7,8,9])
a = arr.reshape(3,3)
for i in range(0,len(a)):
    a[i]=a[i][::-1]

print(a)