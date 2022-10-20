from fractions import Fraction

def P(event, space):
    return Fraction(len(event), len(space))

S = [('Thanh','Nữ'),('Hồng','Nữ'),('Thương','Nữ'),('Đào','Nữ'),('My','Nữ'),('Yến','Nữ'),
     ('Hạnh','Nữ'),('My','Nữ'),('Vy','Nữ'),('Tiên','Nữ'),('Thanh','Nam'),('Thanh','Nam'),
     ('Bình','Nam'),('Nhật','Nam'),('Hào','Nam'),('Đạt','Nam'),('Minh','Nam')]
A = [i for i in S if i[0] == 'Thanh']
B = [i for i in S if i[1] == 'Nữ']
A_B = set(A)&set(B)
P_A = P(A,S)
print(P_A)
P_B = P(B,S)
print(P_B)
P_A_B = P(A_B,S)
print(P_A_B)
E = P(A_B,B)
print(E)