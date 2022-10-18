import itertools
A = {1,2,3,4,5}
k = 3
n = len(A)
num_3_digit = list(itertools.permutations(A,k))
num_length = len(num_3_digit)
print("Num length = {}".format(num_length))