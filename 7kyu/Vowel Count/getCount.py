import re


def getCount(inputStr):
    num_vowels = 0
    # a = (let for let in inputStr if let in "aeiouAEIOU").next()
    pattern = re.compile(r'[aeiou]')
    num_vowels = len(pattern.findall(inputStr))
    # your code here

    return num_vowels


getCount('i am your father')
