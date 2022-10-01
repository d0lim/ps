import sys
from collections import deque


sys.setrecursionlimit(100000)


def dfs(n, h, row, col):
    global rains
    global visited

    visited[row][col] = True

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dr, dc in dirs:
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < n and 0 <= next_col < n:
            if not visited[next_row][next_col] and rains[next_row][next_col] > h:
                dfs(n, h, next_row, next_col)


N = int(input())

rains = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

res = 0

for height in range(0, 101):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and rains[i][j] > height:
                dfs(N, height, i, j)
                cnt += 1
    res = max(res, cnt)

print(res)
