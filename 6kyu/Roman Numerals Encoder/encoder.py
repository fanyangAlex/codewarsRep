def solution(n):
    t = int(n/1000)
    h = int(n % 1000/100)
    c = int(n % 100/10)
    d = int(n % 10)
    res = ''
    for i in range(t):
        res += 'M'

    if h < 4:
        for i in range(h):
            res += 'C'
    elif h == 4:
        res += 'CD'
    elif h == 9:
        res += 'CM'
    else:
        res += 'D'
        for i in range(h-5):
            res += 'C'

    if c < 4:
        for i in range(c):
            res += 'X'
    elif c == 4:
        res += 'XL'
    elif c == 9:
        res += 'XC'
    else:
        res += 'L'
        for i in range(c-5):
            res += 'X'

    if d < 4:
        for i in range(d):
            res += 'I'
    elif d == 4:
        res += 'IV'
    elif d == 9:
        res += 'IX'
    else:
        res += 'V'
        for i in range(d-5):
            res += 'I'

    return res


def solution1(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string
