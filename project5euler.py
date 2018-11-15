import sympy
grid=[i for i in range(11,21)]
def find_no(n):
    return True if all(n%grid[i]==0 for i in range(len(grid))) else False
if __name__ == "__main__":
    no=999
    flag=False
    while flag==False:
        if find_no(no) and sympy.isprime(no)==False:
            print(no)
            flag=True
        no+=1

    

    