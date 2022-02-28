import sys
from collections import deque
from time import sleep


def check_all_visited(visited_grid, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not visited_grid[i][j]:
                return i, j
    return 0, 0


N = int(sys.stdin.readline().rstrip())
grid = [[""] + list(sys.stdin.readline().rstrip()) + [""] for _ in range(N)]
grid = [[""] * (N + 2)] + grid + [[""] * (N + 2)]

regular_count = 0
irregular_count = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[False for _ in range(N + 2)] for _ in range(N + 2)]

while True:
    next_row, next_col = check_all_visited(visited, N)
    if next_row == 0 and next_col == 0:
        break
    else:
        regular_count += 1
        q = deque()
        q.append((next_row, next_col))
        visited[next_row][next_col] = True
        while len(q) > 0:
            row, col = q.popleft()
            for a, b in directions:
                if (
                    grid[row][col] == grid[row + a][col + b]
                    and not visited[row + a][col + b]
                ):
                    q.append((row + a, col + b))
                    visited[row + a][col + b] = True

visited = [[False for _ in range(N + 2)] for _ in range(N + 2)]

while True:
    next_row, next_col = check_all_visited(visited, N)
    if next_row == 0 and next_col == 0:
        break
    else:
        irregular_count += 1
        q = deque()
        q.append((next_row, next_col))
        visited[next_row][next_col] = True
        while len(q) > 0:
            row, col = q.popleft()
            for a, b in directions:
                if grid[row][col] == "R" or grid[row][col] == "G":
                    if (
                        grid[row + a][col + b] == "R" or grid[row + a][col + b] == "G"
                    ) and not visited[row + a][col + b]:
                        q.append((row + a, col + b))
                        visited[row + a][col + b] = True
                else:
                    if (
                        grid[row][col] == grid[row + a][col + b]
                        and not visited[row + a][col + b]
                    ):
                        q.append((row + a, col + b))
                        visited[row + a][col + b] = True
print(regular_count, irregular_count)
