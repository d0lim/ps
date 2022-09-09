import sys
from collections import deque


def check_cheese(board, n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != 0:
                return True
    return False


N, M = map(int, sys.stdin.readline().rstrip().split())


board = [[-1] * (M + 2)]
for _ in range(N):
    board.append(
        [-1]
        + list(
            map(
                int,
                sys.stdin.readline().rstrip().split(),
            )
        )
        + [-1]
    )
board.append([-1] * (M + 2))


res = 0
while check_cheese(board, N, M):
    check = [[0] * (M + 2) for _ in range(N + 2)]
    q = deque()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q.append((1, 1))

    while q:
        curr_row, curr_col = q.popleft()

        for dr, dc in dirs:
            next_row = curr_row + dr
            next_col = curr_col + dc
            if board[next_row][next_col] == 0 and check[next_row][next_col] == 0:
                q.append((next_row, next_col))
                check[next_row][next_col] += 1
            elif board[next_row][next_col] == 1:
                check[next_row][next_col] += 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if check[i][j] >= 2:
                board[i][j] = 0

    res += 1

print(res)
