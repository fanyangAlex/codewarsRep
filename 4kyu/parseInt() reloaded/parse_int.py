import re
def parse_int(string):
    if string=='one million':
        return 1000000
    dic={
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,
        'eleven':11,
        'twelve':12,
        'thirteen':13,
        'fourteen':14,
        'fifteen':15,
        'sixteen':16,
        'seventeen':17,
        'eighteen':18,
        'nineteen':19,
        'twenty':20,
        'thirty':30,
        'forty':40,
        'fifty':50,
        'sixty':60,
        'seventy':70,
        'eighty':80,
        'ninety':90
    }
    mut={
        'hundred':100,
    }
    string=re.sub(r'-',' ',string)
    arr=string.split('thousand')
    first=0
    second=0
    for word in arr[0].split(' '):
        if word in dic:
            first=first+dic[word]
        elif word in mut:
            first=first*mut[word]
    if len(arr)==1:
        return first
    else:
        for word in arr[1].split(' '):
            if word in dic:
                second=second+dic[word]
            elif word in mut:
                second=second*mut[word]
        return first*1000+second
    

print(parse_int('two hundred forty-six'))