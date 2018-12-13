import math


def comp(array1, array2):
    if len(array1) == 0 and len(array2) == 0:
        return True
    elif len(array1) == 0 or len(array2) == 0:
        return False
    else:
        array1.sort()
        array2.sort()
        print(array1, array2)
        for i in range(len(array1)):
            print(i)
            if(array1[i]*array1[i] != array2[i]):
                return False
            pass
        return True
    # your code


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print comp(a1, a2)
