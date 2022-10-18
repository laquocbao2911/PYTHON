from itertools import product
import random
ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
suits = {'♡', '♢', '♣', '♠'}
cards = list(product(ranks , suits))
def simualtor_poker2(n):
    count = 0
    for i in range(n):
        temp = random.sample(cards,4)
        arr = []
        for j in temp:
            arr.append(j[1])
        if len(set(arr)) == 4: count+=1
    return count/n
print(simualtor_poker2(1000))