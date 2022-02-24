import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = (
    [[0] * (M + 2)]
    + [[0] + list(map(int, sys.stdin.readline().rstrip())) + [0] for _ in range(N)]
    + [[0] * (M + 2)]
)
visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]
result = [[100000 for _ in range(M + 2)] for _ in range(N + 2)]

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

q = deque()
q.append((1, 1))
result[1][1] = 1
visited[1][1] = True

while len(q) != 0:
    row, col = q.popleft()
    if row != 1 or col != 1:
        result[row][col] = min([result[row + a][col + b] for a, b in directions]) + 1
    for a, b in directions:
        if maze[row + a][col + b] == 1 and not visited[row + a][col + b]:
            q.append((row + a, col + b))
            visited[row + a][col + b] = True


print(result[N][M])
