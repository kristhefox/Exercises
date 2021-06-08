# ex2_2

from itertools import permutations

def perm(x):
    """ this function generates all permutations of x """
    l = list(permutations(x))
    print(l)