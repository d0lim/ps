import sys
from collections import deque, defaultdict

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

count = 0

for i in range(1, N + 1):
    if not visited[i] > 0:
        visited[i] = True
        s = deque()
        for adj in graph[i]:
            s.append(adj)
        while s:
            curr = s.pop()
            visited[curr] = True
            for adj in graph[curr]:
                if not visited[adj]:
                    s.append(adj)

        count += 1

print(count)
