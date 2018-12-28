def permutations(string):
    if len(string)==1:
        return [string]
    dic={}
    res=[]
    for index in range(len(string)):
        if string[index] not in dic:
            dic[string[index]]=True
            cres=permutations(string[:index]+string[index+1:])
            for item in cres:
                res.append(string[index]+item)
    
    return res