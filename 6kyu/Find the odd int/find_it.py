def find_it(seq):
    a = set()
    for num in seq:
        if num in a:
            a.remove(num)
        else:
            a.add(num)

    return a.pop()


find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
