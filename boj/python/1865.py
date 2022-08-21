import sys
from collections import defaultdict, deque


def bellman_ford(n, start, adj):
    result = [10e9] * (n + 1)
    result[start] = 0
    for i in range(n):
        for curr_v in range(1, n + 1):
            for next_v, next_w in adj[curr_v]:
                if result[curr_v] + next_w < result[next_v]:
                    result[next_v] = result[curr_v] + next_w
                    if i == n - 1:
                        return result
    return None


tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    N, M, W = map(int, sys.stdin.readline().rstrip().split())

    adjacency = defaultdict(list)
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        adjacency[S].append((E, T))
        adjacency[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        adjacency[S].append((E, -T))

    result = "NO"
    if bellman_ford(N, 1, adjacency) is not None:
        result = "YES"

    print(result)
