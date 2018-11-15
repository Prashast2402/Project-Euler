from functools import reduce
def factor(n):
    return len(set(reduce(list.__add__,([i,n//i]for i in range(1,int(n**0.5)+1)if n%i==0))))
if __name__ == "__main__":
    count=0
    no=1
    i=1
    while count<500:
        count=factor(no)
        i=i+1
        no=no+i
print(no-i)
