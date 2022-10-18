import numpy as np

x = np.array([3,11,-9,-131,-1,1,-11,91,-6,407,-12,-11,12,153,371])

#Câu a
print("Maximun = "+str(max(x)))

#Câu b
print("Minimun = "+str(min(x)))

# Câu c
for i in range(0,len(x)):
    if x[i] >= 10:
        print("the index of the values of x that are greater than 10: %d"%(i))
# Câu d
print("Reverse vector = "+str(x[::-1]))

# Câu e
print("ascending order")
print(np.sort(x))

# Câu f
print("descending order")
print(-np.sort(-x))

# Câu g
count = 0
for i in range(0,len(x)):
    for j in range(0,len(x)):
        if i!=j and (x[i]+x[j])==0:
            count+=1
print("times have xi + xj = 0 : %d"%(count))

# Câu h
total = 0
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i] == x[j]:
            total += x[i]
print("total number of duplicate elements = %d"%(total))

# Câu i
lst = []
for i in range(0,len(x)):
    yi = x[i] + x[len(x)-i-1]
    lst.append(yi)
print("Vector y = "+str(np.array(lst)))

# Câu j
def checkAms(x):
    count = result = 0
    temp = x
    while x>0:
        x//=10
        count+=1
    while temp>0:
        result += (temp%10)**count
        temp //=10
    return result
cauj = []
for i in range(0,len(x)):
    if checkAms(x[i]) == x[i]:
        cauj.append(x[i])
print("Armstrong/Narcissistic number = "+str(cauj))

# Câu k
k = []
for i in x:
    if i >= 0:
        k.append(i)
print("Positive number = "+str(np.array(k)))

# Câu l
middle = 0
l = np.sort(x)
if len(x)%2==1:
    middle = l[len(x)//2]
elif len(x)%2==0:
    middle = (l[len(x)//2-1]+l[(len(x)//2)])/2
print("Median value in vector x = %d"%(middle))

# Câu m
m = 0
dtb = sum(x)/len(x)
for i in x:
    if i < dtb:
        m += i
print("sum of all values which are less than mean value in x vector = %d"%(m))

# Câu n
for i in range(0,len(x)):
    if x[i] < 0:
        x[i] = -x[i]
print("New vector = "+str(x))