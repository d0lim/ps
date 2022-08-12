import sys
from collections import defaultdict
import heapq

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())

adjacency = defaultdict(list)


def djikstra(n, start, adj):
    heap = []
    result = [float("inf")] * (n + 1)

    heapq.heappush(heap, (0, start))
    result[start] = 0

    while heap:
        curr_w, curr_v = heapq.heappop(heap)

        if result[curr_v] < curr_w:
            continue

        next_adjs = adj[curr_v]
        for a, w in next_adjs:
            next_w = curr_w + w
            if next_w < result[a]:
                heapq.heappush(heap, (next_w, a))
                result[a] = next_w

    return result


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    adjacency[u].append((v, w))

res = djikstra(V, K, adjacency)
for r in list(map(lambda x: x if x != float("inf") else "INF", res))[1:]:
    print(r)
