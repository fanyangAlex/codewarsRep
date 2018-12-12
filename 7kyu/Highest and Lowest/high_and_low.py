def high_and_low(numbers):
    array = numbers.split(' ')
    high = int(array[0])
    low = int(array[0])
    for item in array:
        intItem = int(item)
        if intItem > high:
            high = intItem
        if intItem < low:
            low = intItem
        pass
    return str(high)+' '+str(low)


high_and_low('1 2 3 4')
