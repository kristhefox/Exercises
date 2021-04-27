# ex1_2

def factorial(n):
    """ this function returns factorial of entered number """
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        raise ValueError
    else:
        return n * factorial(n-1)