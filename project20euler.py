fact=[0]*500
fact[0]=1
def compute(n):
    count=1
    for i in range(2,n+1):
        count=multiply(i,count)
def multiply(n,limit):
    carry=0
    for i in range(0,limit):
        temp=fact[i]*n+carry
        fact[i]=temp%10
        carry=temp//10
    while (carry):
        fact[limit]=carry%10
        carry=carry//10
        limit=limit+1
    return limit
compute(100)
print(sum(fact))