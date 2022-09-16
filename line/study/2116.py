import sys
from copy import deepcopy

# A - F, 0 - 5
# B - D, 1 - 3
# C - E, 2 - 4

opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

# 완탐 해버리자.

n = int(input())
dices = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

res = 0

for i in range(6):
    temp = deepcopy(dices)
    bottom_idx = i
    for j in range(n):
        temp[j][bottom_idx] = 0
        curr_top = temp[j][opposite[bottom_idx]]
        temp[j][opposite[bottom_idx]] = 0
        if j < n - 1:
            bottom_idx = temp[j + 1].index(curr_top)
    res = max(res, sum(map(max, temp)))

print(res)
