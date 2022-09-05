import sys
from itertools import combinations

T = int(input())

for _ in range(T):
    N = int(input())
    score_sets = [
        tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)
    ]
    sorted_sets = list(sorted(score_sets, key=lambda x: x[0]))
    cnt = 0
    interview = float("inf")
    for i in range(N):
        if sorted_sets[i][1] < interview:
            cnt += 1
            interview = sorted_sets[i][1]

    print(cnt)
