def iq_test(numbers):
    array = list(map(lambda v: int(v), numbers.split(' ')))
    length = len(array)
    isEven = sum(1 for a in array if a % 2 == 0) > 1
    for i in range(length):
        if (isEven and array[i] % 2 == 1)or(not isEven and array[i] % 2 == 0):
            return i+1


def iq_test1(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


iq_test("2 4 7 8 10")
