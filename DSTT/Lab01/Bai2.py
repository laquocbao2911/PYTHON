di = {1:"apple",2:"banana",3:"kiwi",4:"orange"}
# Câu a
lst = []
for i in di.keys():
    lst.append(di[i])
print(lst)
# Câu b
print(tuple(di.values()))
# Câu c
print(set(di.values()))
