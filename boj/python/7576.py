import sys
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, sys.stdin.readline().rstrip().split())

box = [[-1 for _ in range(M + 2)]]

for _ in range(N):
    box.append([-1] + list(map(int, sys.stdin.readline().rstrip().split())) + [-1])

box.append([-1 for _ in range(M + 2)])


visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]

# need time-series thinknig
# this means, queue data need to include time data
t = 0
q = deque()

# first exploration
for r in range(1, N + 1):
    for c in range(1, M + 1):
        if box[r][c] == 1:
            visited[r][c] = True
            q.append((r, c, t))

# bfs
while q:
    row, col, curr_t = q.popleft()
    t = curr_t

    for dr, dc in dirs:
        if not visited[row + dr][col + dc] and box[row + dr][col + dc] == 0:
            box[row + dr][col + dc] = 1
            visited[row + dr][col + dc] = True
            q.append((row + dr, col + dc, curr_t + 1))

# validate all tomato is matured
mature = True
outer_break = False
for r in range(1, N + 1):
    for c in range(1, M + 1):
        if box[r][c] == 0:
            mature = False
            outer_break = True
            break
    if outer_break:
        break

if not mature:
    print(-1)
else:
    print(t)
