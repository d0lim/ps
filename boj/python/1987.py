import sys


def dfs(r, c, row, col, cnt):
    global res
    global alp
    global visited

    visited[ord(alp[row][col]) - 65] = True
    res = max(res, cnt)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dr, dc in dirs:
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < r and 0 <= next_col < c:
            if not visited[ord(alp[next_row][next_col]) - 65]:
                dfs(r, c, next_row, next_col, cnt + 1)
    visited[ord(alp[row][col]) - 65] = False


R, C = map(int, input().split())

alp = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [False] * 26

res = 0
dfs(R, C, 0, 0, 1)

print(res)
