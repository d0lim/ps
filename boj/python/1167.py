import sys
from collections import deque


max_length = 0
max_vertex = 0


V = int(sys.stdin.readline().rstrip())

vertices = dict()

for _ in range(V):
    info = list(map(int, sys.stdin.readline().rstrip().split()))[:-1]
    vertex = info[0]
    connections = info[1:]
    iter_count = len(connections) // 2
    for i in range(iter_count):
        vertices.setdefault(vertex, [])
        vertices[vertex].append([connections[i * 2], connections[i * 2 + 1]])


def dfs(vertex, length, visited, vertices):
    global max_length
    global max_vertex
    if length > max_length:
        max_length = length
        max_vertex = vertex

    visited[vertex] = True

    for v, l in vertices[vertex]:
        if not visited[v]:
            dfs(v, length + l, visited, vertices)


visited = [False for _ in range(V + 1)]
dfs(1, 0, visited, vertices)
visited = [False for _ in range(V + 1)]
dfs(max_vertex, 0, visited, vertices)
print(max_length)
