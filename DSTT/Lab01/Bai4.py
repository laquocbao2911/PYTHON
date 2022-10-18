s1 = {1,2,4,6,7}
s2 = {0,1,2,3,4,8}

caua = {0}
# Câu a
caua.clear()
for i in s1:
    for j in s2:
        if j == i:
            caua.add(j)
print(caua)
# Câu b
caub = s1
for i in s2:
    caub.add(i)
print(caub)
# Câu c
x = 10
cauc = s2
cauc.update({x})
print(cauc)
# Câu d
x = 4
caud = s1
caud.remove(x)
print(caud)