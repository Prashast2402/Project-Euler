import sympy
grid=[i for i in range(1,1000000) if sympy.isprime(i)]
print(grid[10000])