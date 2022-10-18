import itertools
def cross(A,B):
    return {a+b for a in A for b in B}
urn = cross('W','12345678') | cross('R','123456789') | cross('B','123456')
U3 = list(itertools.combinations(urn,3))
len_U3 = len(U3)
print('Cau a')
print(U3)
print(len_U3)

#Cau b
print('Cau b')
for temp in U3:
    if temp[0][0] != temp[1][0] and temp[0][0] != temp[2][0] and temp[1][0] != temp[2][0]:
        print(temp)

#Cau c
print('Cau c')
check = 0
for i in U3:
    if i[0][0] == 'W' and i[1][0] == 'R':
        check += 1
print(check)