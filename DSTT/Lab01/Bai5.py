import matplotlib .pyplot as plt
import numpy as np

lst = [1, 4, 6, 8, 22, 11, 10, 3, 6]
temp = []
for i in np.arange(len(lst)):
    temp.append(str(i))
print(temp)
plt.bar(np.arange(len(lst)),lst,color="m")
plt.xticks(np.arange(len(lst)),temp)
plt.show()