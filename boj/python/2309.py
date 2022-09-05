import sys
from itertools import combinations

heights = [int(sys.stdin.readline().rstrip()) for _ in range(9)]

combs = list(combinations(heights, 7))

sums = map(sum, combs)
for i, s in enumerate(sums):
    if s == 100:
        for h in sorted(combs[i]):
            print(h)
        break
