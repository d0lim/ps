import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

visited = [False] * 100001

q = deque()

q.append(N)
visited[N] = True

t = [0] * 100001
while q:
    current = q.popleft()

    available = list(
        filter(lambda x: 0 <= x <= 100000, [current - 1, current + 1, current * 2])
    )

    for next_position in available:
        if not visited[next_position]:
            visited[next_position] = True
            q.append(next_position)
            t[next_position] = t[current] + 1

        if next_position == K:
            q = []
            break

print(t[K])
