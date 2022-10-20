from fractions import Fraction
from itertools import *
import random
def P(event, space):
    return Fraction(len(event), len(space))

ranks = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['♠','♡', '♢','♣']
cards = []
for i in ranks:
    for j in suits:
        temp = str(i) + j
        cards.append(temp)
B = list(permutations(cards,3))
print(B)
A1 = {i for i in B if ''.join(i).count('K') in {1,2}}
A2 = {i for i in B if ''.join(i).count('K')>=1}
P_A1 = round(P(A1,B),4)
P_A2 = round(P(A2,B),4)
