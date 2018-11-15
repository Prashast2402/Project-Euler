def istrip(a,c,b):
    return True if a+b==c else False
for i in range(1,500):
    for j in range(1,500):
        for k in range(1,500):
            if i+j+k==1000:
                if istrip(i*i,j*j,k*k):
                       pro=i*j*k
                       print(i*j*k)
                       break
