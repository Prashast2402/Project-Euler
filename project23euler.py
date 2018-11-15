from functools import reduce
from itertools import combinations_with_replacement
import time
a=time.time()
def fact(n):
    return set(reduce(list.__add__,([i,n//i]for i in range(1,int(n**0.5)+1)if n%i==0)))
if __name__ == "__main__":
    grid=[]
    for i in range(12,28124):
        no=sum(fact(i))
        no=no-i
        if no!=i and no>i:
            grid.append(i)
    grid1=[i for i in range(1,28124)]
    x=set()
    for s in combinations_with_replacement(grid,2):
        if sum(s)<28124:
            x.add(sum(s))
    print(sum(grid1)-sum(x))
    print(time.time()-a)


    





