import sys
from collections import deque, defaultdict

N, M, V = map(int, sys.stdin.readline().rstrip().split())

adjacent = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

for key in adjacent.keys():
    adjacent[key].sort()

# DFS
s = deque()
visited = [False] * (N + 1)
dfs = []
s.append(V)
while len(s) > 0:
    current = s.pop()
    if not visited[current]:
        visited[current] = True
        dfs.append(current)

    for n in adjacent[current][::-1]:
        if not visited[n]:
            s.append(n)

# BFS
q = deque()
visited = [False] * (N + 1)
bfs = []
visited[V] = True
q.append(V)
bfs.append(V)
while len(q) > 0:
    current = q.popleft()

    for n in adjacent[current]:
        if not visited[n]:
            visited[n] = True
            bfs.append(n)
            q.append(n)

print(" ".join(map(str, dfs)))
print(" ".join(map(str, bfs)))
