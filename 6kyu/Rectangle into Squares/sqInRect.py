def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    big = max(lng, wdth)
    small = min(lng, wdth)
    result = []
    while small > 0:
        result.append(small)
        small = min(big-small, small)
        big = max(big-small, small)
    return result


sqInRect(14, 4)
