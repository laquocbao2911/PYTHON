import numpy as np

x = np.array([])

n = int(input("Enter n: "))
for i in range(1,n+1):
    x = np.append(x,pow(10,i))
print("x = "+str(x))