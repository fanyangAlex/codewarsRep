def thirt(n):
    s=str(n)
    list1=[1,10,9,12,3,4]
    sum=0
    for i in reversed(range(len(s))):
        sum+=int(s[i])*list1[(len(s)-1-i)%6]
      
        pass
    if sum==n:
        return sum
    else:
        return thirt(sum)
    # your code

print(thirt(1234567)