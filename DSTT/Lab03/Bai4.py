import numpy as np
import random

arr = np.array([1,2,3,4,5,6,7,8,9])
a = arr.reshape(3,3)
b = []
b = a[::-1]
print(b)