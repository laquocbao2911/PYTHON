di = {1:"apple",2:"banana",3:"kiwi",4:"orange",5:"banana",6:"banana"}
inp = input("Enter x : ")
# Câu a
count = 0
for i in di.keys():
    if inp == di[i]:
        count+=1
print(str(inp) + " xuất hiện "+str(count)+" lần.")
# Câu b
k = input("Enter k :")
for i in di.keys():
    if inp == di[i]:
        di[i] = k
print(di)
# Câu c
di = {1:"apple",2:"banana",3:"kiwi",4:"orange",5:"banana",6:"banana"}
for i in range (1,len(di.keys())+1):
    if inp == di[i]:
        di.pop(i)
print(di)
# Câu d
di = {1:"apple",2:"banana",3:"kiwi",4:"orange",5:"banana",6:"banana"}
x = "coconut"
di[7]=x
print(di)