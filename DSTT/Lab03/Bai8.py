import numpy as np
import random

sale = np.array([[12,15,10,16,12],[5,9,14,7,10],[8,12,10,9,15]])
money = [2,1,3]
for i in range(0,len(sale)):
    sale[i] *= money[i]
print(np.sum(sale,axis=0))