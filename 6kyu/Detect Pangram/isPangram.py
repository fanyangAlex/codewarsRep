import string

def is_pangram(s):
    num = sum(1 for str in 'abcdefghijklmnopqrstuvwxyz' if str in s.lower())
    return num == 26

def is_pangram2(s):
    print(set(s.lower()))
    return set(string.ascii_lowercase) <= set(s.lower())

is_pangram2('The quick brown fox jumps over the lazy dog')
