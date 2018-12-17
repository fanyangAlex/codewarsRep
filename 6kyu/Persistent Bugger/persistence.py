from functools import reduce


def persistence(n):
    times = 0
    while n > 9:
        nextN = reduce(lambda a, b:  int(a)*int(b), str(n))
        n = nextN
        times = times+1
        pass
    return times
    # your code
