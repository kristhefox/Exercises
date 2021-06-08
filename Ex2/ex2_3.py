# ex2_3

from itertools import permutations

def password(x, *args):
# this function generates all combinations of string
    chars=args
    l=list(permutations(chars,x))
    print(l)

password(3,'a','b')