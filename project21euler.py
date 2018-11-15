def check(n):
    tot=0
    for i in range(1,n):
        if n%i==0:
            tot=tot+i
    return tot
if __name__ == "__main__":
    grid=[]
    for i in range(1,10001):
        if i in grid:
            continue
        else:
            n=check(i)
            x=check(n)
        if x==i and n!=i:
            print(i)
            grid.append(i)
            grid.append(n)
print(sum(grid))