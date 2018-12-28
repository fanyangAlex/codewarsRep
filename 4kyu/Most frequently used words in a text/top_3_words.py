import re
def top_3_words(text):
    string= re.sub(r' \'* ',' ', text.lower())
    string=re.sub(r'[^a-z|\']',' ', string).split(' ')
    arr=[]
    for i in string:
        if i!='':
            arr.append(i)
    dic={}
    for i in arr:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
   
    return [key for key,value in sorted(dic.items(),key=lambda x: x[1],reverse=True) ][:3]

print(top_3_words(" '  ' //wont won't won't d d d"))