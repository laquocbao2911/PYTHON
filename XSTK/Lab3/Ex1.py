from fractions import Fraction

def P(event, space):
    return Fraction(len(event&space), len(space))
#Câu a
S = {'MMM','MMF','MFM','MFF','FFF'}
#Câu b
space_S = len(S)
# Câu c
B = {i for i in S if 'F' in i}
print(B)
#Câu d
A = {i for i in S if i.count('M') == 3}
print(A)
#Câu e
temp_E = {'FFF'}
E = P(temp_E,B)
print(E)