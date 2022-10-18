from itertools import product
import random
ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
suits = {'♡', '♢', '♣', '♠'}
cards = list(product(ranks , suits))
def simualtor_poker1(n):
    count = 0
    for i in range(n):
        temp = random.sample(cards,5)
        spt = 0
        for j in temp:
            if j[1] == '♡': spt += 1
        if spt == 5: count+=1
    return count/n
print(simualtor_poker1(1000))