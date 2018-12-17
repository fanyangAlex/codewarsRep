def add(a):
    return AddValue(a)


class AddValue(object):
    def __init__(self, *args):
        self.value = args[0]
        pass

    def __call__(self, x):
        return AddValue(self.value+x)

    def __eq__(self, x):
        return self.value == x

    def __add__(self, x):
        return self.value+x

    def __sub__(self, x):
        return self.value+x


print(add(1)(2) == 3)
