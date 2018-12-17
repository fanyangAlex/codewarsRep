def namelist(names):
    res = ''
    length = len(names)
    if length > 0:
        res += names[0]['name']
        for i in range(length-1):
            if i == length-2:
                res += (' & '+names[i+1]['name'])
            else:
                res += (', '+names[i+1]['name'])

    return res
