def rgb(r, g, b):
    return fixNum(r)+fixNum(g)+fixNum(b)


def fixNum(num):
    s = num
    if num < 0:
        s = 0
    elif num > 255:
        s = 255
    st = str(hex(s))[2:4].upper()
    return st if len(st) == 2 else '0'+st


def rgbC(r, g, b):
    def round(x): return min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(str(hex(20))[2:4])
