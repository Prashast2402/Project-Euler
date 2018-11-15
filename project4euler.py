def check_pallindrome(n):
    return True if n==n[::-1] else False
grid=[]
for i in range(100,1000):
    for j in range(100,1000):
        if check_pallindrome(str(i*j)):
            grid.append(i*j)
print(max(grid))