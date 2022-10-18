import numpy as np

x = np.array([0,2,4,6,8,10,12,14,16,18,20])

# Câu a
print("Câu a = "+str(x[0:6:1]))

# Câu b
print("Câu b = "+str(x[::-1][0:5]))

# Câu c
c = [x[0],x[3],x[-1]]
print("Câu c = "+str(np.array(c)))

# Câu d
d = [x[0],x[2],x[4],x[6]]
print("Câu d = "+str(np.array(d)))

# Câu e
e = []
for i in x:
    if i%2==1:
        e.append(i)
print("Câu e = "+str(np.array(e)))

# Câu f
f = []
for i in x:
    if i%2==0:
        f.append(i)
print("Câu f = "+str(np.array(f)))