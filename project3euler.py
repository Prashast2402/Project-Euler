import sympy
def factors(n):
    grid=[i for i in range(2,int(n**0.5)) if n%i==0 and sympy.isprime(i) ]
    return grid
grid=factors(600851475143)
print(max(grid))






