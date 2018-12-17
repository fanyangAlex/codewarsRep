def recoverSecret(triplets):
    res = ''
    while len(triplets) > 0:
        dic = {}
        for trip in triplets:
            for l in range(len(trip)):
                if trip[l] not in dic or dic[trip[l]] < l:
                    dic[trip[l]] = l

        string = list(dic.keys())[list(dic.values()).index(0)]
        res += string
        for l in range(len(triplets)):
            if string in triplets[l]:
                triplets[l].pop(0)
        triplets = list(filter(lambda v: len(v) > 0, triplets))

    return res


def recoverSecretC(triplets):
    r = list(set([i for l in triplets for i in l]))
    for l in triplets:
        fix(r, l[1], l[2])
        fix(r, l[0], l[1])
    return ''.join(r)


def fix(l, a, b):
    """let l.index(a) < l.index(b)"""
    if l.index(a) > l.index(b):
        l.remove(a)
        l.insert(l.index(b), a)


secret = "whatisup"
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]
recoverSecret(triplets)
