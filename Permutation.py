from itertools import *

S = "HACK"
k = 2
for i in permutations(sorted(S), int(k)):
    print("".join(i))

for i in range(1, int(k)+1):
    for j in combinations(sorted(S),i):
        print("".join(j))