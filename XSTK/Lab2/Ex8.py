import itertools
def cross(A, B):
    return {a + b for a in A for b in B}
def combos(items , n):
    return {' '.join(combo) for combo in itertools.combinations(items , n)}
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
U6 = combos(urn,6)
