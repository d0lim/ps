import sys
from collections import defaultdict
import heapq


def djikstra(n, start, adj):
    heap = []
    res = [float("inf")] * (n + 1)

    res[start] = 0

    heapq.heappush(heap, (0, start))

    while heap:
        curr_cost, curr_vertex = heapq.heappop(heap)

        # Filter
        if res[curr_vertex] < curr_cost:
            continue

        for next_vertex, next_cost in adj[curr_vertex]:
            if curr_cost + next_cost < res[next_vertex]:
                res[next_vertex] = curr_cost + next_cost
                heapq.heappush(heap, (curr_cost + next_cost, next_vertex))

    return res


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

adjacency = defaultdict(list)

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().rstrip().split())
    adjacency[s].append((e, c))

S, E = map(int, sys.stdin.readline().rstrip().split())

print(djikstra(N, S, adjacency)[E])
