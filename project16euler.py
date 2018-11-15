number= 2**1000
n=0
while number >0:
    n=n+(int(number%10))
    number=number/10
print(n)
