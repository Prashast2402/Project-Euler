def istrip(a,c,b):
    return True if (a**2)+(b**2)==(c**2) else False
pro=0
for i in range(100,1000):
    for j in range(100,1000):
        for k in range(100,1000):
            if istrip(i,j,k):
                if i+j+k==1000:
                    pro=i*j*k
print(pro)