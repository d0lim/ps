import sys

N = int(input())

board = [0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0]

max_res = [[0] * 5 for _ in range(2)]
min_res = [[float("inf")] * 5 for _ in range(2)]

max_res[0][1] = board[1]
max_res[0][2] = board[2]
max_res[0][3] = board[3]

min_res[0][1] = board[1]
min_res[0][2] = board[2]
min_res[0][3] = board[3]

for _ in range(1, N):
    board = [0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0]
    for j in range(1, 4):
        max_res[1][j] = board[j] + max(
            max_res[0][j - 1], max_res[0][j], max_res[0][j + 1]
        )
        min_res[1][j] = board[j] + min(
            min_res[0][j - 1], min_res[0][j], min_res[0][j + 1]
        )
    for j in range(1, 4):
        max_res[0][j] = max_res[1][j]
        min_res[0][j] = min_res[1][j]

print(max(max_res[0][1:4]), min(min_res[0][1:4]))
