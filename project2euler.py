def check_even(n):
    if n%2==0:
        return n
    else:
        return 0
def fact():
    a=0
    b=1
    c=a+b
    tot=0
    while c<4000000:
        a=b
        b=c
        c=a+b
        tot=tot+(check_even(c))
    return(tot)
print(fact())