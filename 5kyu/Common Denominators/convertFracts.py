import functools


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a,  b):
    return a*b/gcd(a, b)


def convertFracts(lst):
    time = list(pair[1] for pair in lst)
    temp = int(functools.reduce(lcm, time))

    return list([int(temp/pair[1])*pair[0], temp] for pair in lst)


a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
convertFracts(a)
