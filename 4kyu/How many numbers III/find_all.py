def find_all(sum_dig, digs):
    res=[]
    if digs*9>=sum_dig:
        sum=0
        min=0
        max=0
        for i in range(int(sum_dig/digs)):
            first=i+1
            tres=find_all_small(sum_dig-first,digs-1,first)
            if len(tres)>0:
                sum=sum+tres[0]
                if min==0:
                    min=int(str(first)+str(tres[1]))
                max=int(str(first)+str(tres[2]))
            
            res=[sum,min,max]
    return res

def find_all_small(sum_dig, digs,top):
    res=[]
    if digs*9>=sum_dig:
        if digs==1:
            if sum_dig>=top:
                return [1,sum_dig,sum_dig]
            else: 
                return []
        sum=0
        min=0
        max=0
        for i in range(top-1,int(sum_dig/digs)):
            first=i+1
            tres=find_all_small(sum_dig-first,digs-1,first)
            if len(tres)>0:
                sum=sum+tres[0]
                if min==0:
                    min=int(str(first)+str(tres[1]))
                max=int(str(first)+str(tres[2]))
            
            res=[sum,min,max]
    return res
    
print(find_all(35,6))