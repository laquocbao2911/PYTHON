lst = [0,5,7,9]
d = {}
print(lst)
#Câu a
print(tuple(lst))
# Câu b
print(set(lst))
# Câu c
for i in range(0,len(lst)):
    d[i] = lst[i]
print(d)
