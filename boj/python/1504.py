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
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adjacency[a].append((b, c))
    adjacency[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().rstrip().split())

res = min(
    dijkstra(N, 1, v1, adjacency)
    + dijkstra(N, v1, v2, adjacency)
    + dijkstra(N, v2, N, adjacency),
    dijkstra(N, 1, v2, adjacency)
    + dijkstra(N, v2, v1, adjacency)
    + dijkstra(N, v1, N, adjacency),
)

print(res if res < float("inf") else -1)
