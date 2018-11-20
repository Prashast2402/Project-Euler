from sympy import isprime
import itertools
from timeit import default_timer as timer
def find_limit(a,b):
    n=0
    count=0
    while isprime((n**2)+(a*n)+b):
        count+=1
        n+=1
    return count
start=timer()
a=[i for i in range(-1000,1001)]
re=itertools.combinations_with_replacement(a,2)
m=0
pro=0
for i in re:
    no=find_limit(i[0],i[1])
    if no>m:
        m=no
        pro=i[0]*i[1]
        n=[0]
        b=i[1]
print(pro)
print(timer()-start)
    
    