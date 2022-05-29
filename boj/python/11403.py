import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline().rstrip())

G = defaultdict(list)

for i in range(N):
    adjacents = list(map(int, sys.stdin.readline().rstrip().split()))
    for j, v in enumerate(adjacents):
        if v == 1:
            G[i].append(j)

reachable = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    s = deque()
    visited = [False] * N

    # dfs
    for adj in G[i]:
        s.append(adj)

    while s:
        curr = s.pop()
        reachable[i][curr] = 1
        visited[curr] = True

        for adj in G[curr]:
            if not visited[adj]:
                s.append(adj)

for r in reachable:
    print(" ".join(map(str, r)))
