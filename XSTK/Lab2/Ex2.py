from more_itertools import random_combination
from sympy import true

import random
def oddCheck(n):
    if n%2!=0:
        return True
    return False

def simulator_dice2(n):
    count = 0
    for i in range(0,n):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if oddCheck(d1) and oddCheck(d2):
            count +=1
    return count/n

print(simulator_dice2(10))