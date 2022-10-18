from more_itertools import random_combination
import random
def simulator_dice5(n):
    count = 0
    for i in range(0,n):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if d1 + d2 > 6:
            count +=1
    return count/n

print(simulator_dice5(10))