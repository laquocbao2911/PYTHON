import itertools
def cross(A,B):
    return {a+b for a in A for b in B}
bookMaths = cross('M','1234')
toan = list(itertools.permutations(bookMaths,4))
bookPhys = cross('P','123')
ly = list(itertools.permutations(bookPhys,3))
bookChemistry = cross('C','12')
hoa = itertools.permutations(bookChemistry,2)
tienganh = cross('L','1')
arr = []
for i in toan:
    arr.append(i)
# result = list(itertools.permutations(arr,4))
print(arr)