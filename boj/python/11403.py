from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

vertices = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

adjacent = dict()
for idx, vertex in enumerate(vertices):
    adjacent.setdefault(idx, [])
    for i, v in enumerate(vertex):
        if v == 1:
            adjacent[idx].append(i)


for key, adj_vertices in adjacent.items():
    q = deque()
    for adj_vertex in adj_vertices:
        q.append(adj_vertex)
    visited = [False for _ in range(N)]
    visited[key] = True
    while len(q) > 0:
        current_vertex = q.pop()
        visited[current_vertex] = True
        vertices[key][current_vertex] = 1
        for next_vertex in adjacent[current_vertex]:
            if not visited[next_vertex]:
                q.append(next_vertex)
            else:
                vertices[key][next_vertex] = 1

for l in vertices:
    print(" ".join(map(str, l)))
