import numpy as np
from sympy import false, fibonacci

a = int(input("Enter n (câu a): "))
print("Câu a")
print("b="+str(np.arange(12,12+a*2,2)))

print("Câu b")
b = int(input("Enter n (câu b): "))
print("c="+str(np.arange(31,31+2*b,2)))

print("Câu c")
c = int(input("Enter n (câu c): "))
print("x="+str(np.arange(-int(c/2),int(c/2)+1,1)))

print("Câu d")
d = int(input("Enter n (câu d): "))
print("y="+str(np.arange(int(d/2),-int(d/2)-1,-1)))

print("Câu e")
e = int(input("Enter n (câu e): "))
z = np.array([])
for i in range(0,e+1):
    re = 10 - 2*i
    z = np.append(z,re)
print("z="+str(z))

print("Câu f")
f = int(input("Enter n (câu f): "))
cauf = np.array([])
for i in range(0,f+1):
    res = 1/(2**i)
    cauf = np.append(cauf,res)
print("w="+(cauf))

print("Câu g")
g = int(input("Enter n (câu g): "))
caug = np.array([])
for i in range(1,g+1):
    caug = np.append(caug,1/fibonacci(i))
print("d="+str(caug))

print("Câu h")
h = int(input("Enter n (câu h): "))
def prime(num):
    result = []
    for i in range(0,num):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                result.append(1/i)
    return result
print("e="+str(np.array(prime(h))))


print("Câu i")
i = int(input("Enter n (câu i): "))
caui = np.array([])
sum = 0
for z in range(1,i+1):
    sum += z
    caui = np.append(caui,sum)
print("a="+str(caui))

print("Câu j")
j = int(input("Enter n (câu j): "))
cauj = []
result = 2
for i in range(0,j+1):
    if(i%2==1 and i!=1 or i==0):
        result = (result+i)
        cauj.append(1/result)
print("n="+str(np.array(cauj)))

print("Câu k")
k = int(input("Enter n (câu k): "))
cauk = np.array([])
for i in range(0,k):
    cauk = np.append(cauk,i/(i+1))
print("p="+str(cauk))

print("Câu l")
l = int(input("Enter n (câu l) : "))
caul = np.array([])
if l > 0 and l <=25:
    for i in range(97,97+l+1):
        caul = np.append(caul,chr(i))
print("o="+str(caul))

print("Câu m")
m = int(input("Enter n (câu m) : "))
caum = np.array([])
if m > 0 and m <=25:
    for i in range(65,65+m+1,3):
        caum = np.append(caum,chr(i))
print("s="+str(caum))