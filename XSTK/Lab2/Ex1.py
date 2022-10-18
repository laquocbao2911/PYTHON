from more_itertools import random_combination
from sympy import true

import random
def evenCheck(n):
    if n%2==0:
        return True
    return False

def simulator_dice1(n):
    count = 0
    for i in range(0,n):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if evenCheck(d1) and evenCheck(d2):
            count +=1
    return count/n

print(simulator_dice1(10))