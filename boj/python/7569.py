import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().rstrip().split())

box = []
box.append([[-1 for _ in range(M + 2)] for _ in range(N + 2)])
for _ in range(H):
    floor = (
        [[-1 for _ in range(M + 2)]]
        + [
            [-1] + list(map(int, sys.stdin.readline().rstrip().split())) + [-1]
            for _ in range(N)
        ]
        + [[-1 for _ in range(M + 2)]]
    )
    box.append(floor)
box.append([[-1 for _ in range(M + 2)] for _ in range(N + 2)])


visited = [[[False for _ in range(M + 2)] for _ in range(N + 2)] for _ in range(H + 2)]
q = deque()

for i in range(1, H + 1):
    for j in range(1, N + 1):
        for k in range(1, M + 1):
            if box[i][j][k] == 1:
                q.append((i, j, k, 0))
                visited[i][j][k] = True

# BFS
directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
result = 0
while len(q) > 0:
    floor, row, col, day = q.popleft()
    box[floor][row][col] = 1
    if len(q) == 0:
        result = day
    for z, y, x in directions:
        if (
            box[floor + z][row + y][col + x] == 0
            and not visited[floor + z][row + y][col + x]
        ):
            q.append((floor + z, row + y, col + x, day + 1))
            visited[floor + z][row + y][col + x] = True


for i in range(1, H + 1):
    for j in range(1, N + 1):
        for k in range(1, M + 1):
            if box[i][j][k] == 0:
                result = -1
                i = H + 1
                j = N + 1
                k = M + 1

print(result)
