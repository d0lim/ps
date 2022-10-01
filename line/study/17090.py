import sys
from collections import deque

dirs = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}


def dfs(maze, n, m, r, c):
    global circular
    visited = [[False] * m for _ in range(n)]
    visited_l = []
    s = deque()
    s.append(((r, c)))
    while s:
        curr_r, curr_c = s.pop()
        visited[curr_r][curr_c] = True
        visited_l.append((curr_r, curr_c))
        if circular[curr_r][curr_c] == -1:
            return False
        elif circular[curr_r][curr_c] == 1:
            return True
        dr, dc = dirs[maze[curr_r][curr_c]]
        next_r, next_c = curr_r + dr, curr_c + dc
        if not ((0 <= next_r < n) and (0 <= next_c < m)):
            for i, j in visited_l:
                circular[i][j] = 1
            return True
        else:
            if visited[next_r][next_c]:
                for i, j in visited_l:
                    circular[i][j] = 1
                return False
            else:
                s.append((next_r, next_c))


N, M = map(int, sys.stdin.readline().rstrip().split())

maze = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
circular = [[0] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if circular[i][j] == 1:
            cnt += 1
            continue
        elif circular[i][j] == -1:
            continue
        elif dfs(maze, N, M, i, j):
            circular[i][j] = 1
            cnt += 1
        else:
            circular[i][j] = -1

print(cnt)
