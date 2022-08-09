import sys
from collections import defaultdict, deque
import heapq


def dijkstra(n, start, end, adjacency_info):
    heap = []
    result = [float("inf")] * (n + 1)
    result[start] = 0

    heapq.heappush(heap, (0, start))
    while heap:
        val, curr = heapq.heappop(heap)

        # 현재 기록된 값이 더 최소 거리라면 skip
        if result[curr] < val:
            continue

        adjacents = adjacency_info[curr]
        for adj, weight in adjacents:
            new_val = weight + val
            if new_val < result[adj]:
                heapq.heappush(heap, (new_val, adj))
                result[adj] = new_val

    return result[end]


N, M, X = map(int, sys.stdin.readline().rstrip().split())

road = defaultdict(list)

for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().rstrip().split())
    road[start].append((end, weight))

res = 0
# dajikstra loop
for i in range(1, N + 1):
    go_to = dijkstra(N, i, X, road)
    come_back = dijkstra(N, X, i, road)
    if res < go_to + come_back:
        res = go_to + come_back

print(res)
