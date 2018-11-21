from timeit import default_timer as timer
from functools import reduce
from itertools import product
start=timer()
numbers=[i for i in range(2,101)]
grid=product(numbers,repeat=2)
final=set()
for i in grid:
    final.add(i[0]**i[1])
print(len(final))
print(timer()-start)


    