def productFib(prod):
    n = 0
    nValue = fib(n)
    nextNValue = fib(n+1)
    temp = nValue*nextNValue
    while temp < prod:
        n = n+1
        nValue = fib(n)
        nextNValue = fib(n+1)
        temp = nValue*nextNValue
    return [nValue, nextNValue, temp == prod]


fibList = {0: 0, 1: 1}


def fib(num):
    if num in fibList:
        return fibList[num]
    res = fib(num-1)+fib(num-2)
    fibList[num] = res
    return res


def productFibC(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]


productFib(4895)
