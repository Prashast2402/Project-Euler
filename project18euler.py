grid=[]
with open("18.txt") as f:
    for line in f:
         values = [int(v) for v in line.split()]
         grid.append(values)
print(grid[14])
for i in range(13,-1,-1):
    for j in range(len(grid[i])):
        if grid[i+1][j]>grid[i+1][j+1]:
            grid[i][j]=grid[i][j]+grid[i+1][j]
        elif grid[i+1][j]<grid[i+1][j+1]:
            grid[i][j]=grid[i][j]+grid[i+1][j+1]
print(grid)

    