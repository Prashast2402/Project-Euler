import math
s=0
for i in range(2,2000000):
    flag=True
    print(s)
    for j in range(2,int(round(math.sqrt(i))+1)):
        if i%j==0:
            flag=False
    if flag==True:
        s+=i
print(s)