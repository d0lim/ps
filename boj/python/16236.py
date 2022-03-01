import sys
from collections import deque
from time import sleep


def bfs(s, start_row, start_col, size, acc):
    global eaten
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque()
    visited = [[False for _ in range(N + 2)] for _ in range(N + 2)]

    count = 0
    q.append((start_row, start_col, count))
    visited[start_row][start_col] = True

    res = []
    while len(q) > 0:
        row, col, count = q.popleft()

        if s[row][col] >= 1 and s[row][col] < size and not eaten[row][col]:
            if size == acc + 1:
                res.append((row, col, count, size + 1, 0))
            else:
                res.append((row, col, count, size, acc + 1))
        else:
            for a, b in directions:
                if (
                    not visited[row + a][col + b]
                    and s[row + a][col + b] != -1
                    and (s[row + a][col + b] <= size)
                ):
                    q.append((row + a, col + b, count + 1))
                    visited[row + a][col + b] = True

    res.sort(key=lambda x: (x[2], x[0], x[1]))

    if len(res) == 0:
        return 0, 0, 0, 0, 0
    else:
        s[res[0][0]][res[0][1]] = 0
        eaten[res[0][0]][res[0][1]] = True
        return res[0]


N = int(sys.stdin.readline().rstrip())

space = [[-1] * (N + 2)]
space += [
    [-1] + list(map(int, sys.stdin.readline().rstrip().split())) + [-1]
    for _ in range(N)
]
space += [[-1] * (N + 2)]
eaten = [[False for _ in range(N + 2)] for _ in range(N + 2)]

s_row = 0
s_col = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if space[i][j] == 9:
            s_row = i
            s_col = j
            space[i][j] = 0

result = 0
baby_shark = 2
acc = 0
while True:
    s_row, s_col, cnt, baby_shark, acc = bfs(space, s_row, s_col, baby_shark, acc)

    result += cnt

    if s_row == 0 and s_col == 0:
        break

print(result)
