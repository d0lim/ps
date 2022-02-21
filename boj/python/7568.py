import sys

N = int(sys.stdin.readline().rstrip())

rank = [1 for _ in range(N)]
wh_list = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for i, wh in enumerate(wh_list):
    for j, other in enumerate(wh_list):
        if i == j:
            continue
        if wh[0] < other[0] and wh[1] < other[1]:
            rank[i] += 1

print(" ".join(map(str, rank)))
