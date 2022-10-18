from more_itertools import random_combination
import random
def simulator_dice4(n):
    count = 0
    for i in range(0,n):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if (d1 == 1 and d2 == 6) or (d1 == 6 and d2 == 1):
            count +=1
    return count/n

print(simulator_dice4(10))