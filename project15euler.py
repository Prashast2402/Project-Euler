import math as m
def no_of_path(x,y):
    no=m.factorial(x)//(m.factorial(x-y) * m.factorial(y))
    return no
n=no_of_path(40,20)
print(int(n))
