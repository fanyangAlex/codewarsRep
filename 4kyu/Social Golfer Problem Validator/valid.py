def valid(a):
    dlen=len(a[0])
    glen=len(a[0][0])
    for day in a:
        if len(day)!=dlen:
            return False
        for group  in day:
            if len(group)!=glen:
                return False
    dic={}
    isFirst=True
    for day in a:
        for group in day:
            for p in range(len(group)):
                char=group[p]
                rest=group[:p]+group[p+1:]
                if isFirst:
                    dic[char]=''
                elif char in dic:
                    for re in rest:
                        if dic[char].find(re)!=-1:
                            return False
                else:
                    return False
                dic[char]=dic[char]+rest
        isFirst=False
    
    return True
                