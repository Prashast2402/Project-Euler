from itertools import permutations
i=1
for x in permutations([i for i in range(10)]):
    if i==1000000:
        print(x)
        break
    i+=1
