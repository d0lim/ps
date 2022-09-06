import sys
from collections import deque, defaultdict
import heapq


def dijkstra(n, start, end, adj):
    heap = []
    res = [float("inf")] * (n + 1)

    res[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        curr_w, curr_v = heapq.heappop(heap)

        if res[curr_v] < curr_w:
            continue

        for next_v, next_w in adj[curr_v]:
            if curr_w + next_w < res[next_v]:
                res[next_v] = curr_w + next_w
                heapq.heappush(heap, (curr_w + next_w, next_v))

    return res[end]


N, E = map(int, sys.stdin.readline().rstrip().split())

adjacency = defaultdict(list)

for _ in range(E):
    s, e, c = map(int, sys.stdin.readline().rstrip().split())

    adjacency[s].append((e, c))
    adjacency[e].append((s, c))

v1, v2 = map(int, sys.stdin.readline().rstrip().split())

s_v1 = dijkstra(N, 1, v1, adjacency)
s_v2 = dijkstra(N, 1, v2, adjacency)
v1_v2 = dijkstra(N, v1, v2, adjacency)
v1_e = dijkstra(N, v1, N, adjacency)
v2_e = dijkstra(N, v2, N, adjacency)


res = min(s_v1 + v1_v2 + v2_e, s_v2 + v1_v2 + v1_e)

print(res if res != float("inf") else -1)
