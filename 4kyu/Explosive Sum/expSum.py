def exp_sum(n):
    return get_sum(n,n)

dic={}

def get_sum(n,m):
    key=str(n)+'_'+str(m)
    if key in dic:
        return dic[key]
    value=0
    if n==1 or m==1:
        value = 1
    elif n<m:
        value = get_sum(n,n)
    elif n==m:
        value = get_sum(n,n-1)+1
    elif n>m:
        value = get_sum(n,m-1)+get_sum(n-m,m)
    dic[key]=value
    return value

def exp_sum1(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n
  for num in range(1,n+1):
    for i in range(num,n+1):
       print(i,num,dp[i],dp[i-num]) 
       dp[i] += dp[i-num]  ## n的m个数字的排列数量=n的m-1个数字的排列数量+n-m的m个数字的排列数量
    print(dp)
    
  return dp[-1]
print(exp_sum1(10))