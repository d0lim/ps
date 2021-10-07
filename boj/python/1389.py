import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

for _ in range(N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            if matrix[i][j] == 1:
                continue
            else:
                for y in [x for x, t in enumerate(matrix[j]) if matrix[j][x] != 0]:
                    if matrix[i][y] != 0:
                        if matrix[i][j] == 0:
                            matrix[i][j] = matrix[i][y] + matrix[j][y]
                        else:
                            matrix[i][j] = min(
                                matrix[i][j], matrix[i][y] + matrix[j][y]
                            )

sol = 0
ans = 999999999
for idx, row in enumerate(matrix):
    if idx == 0:
        continue
    if ans > sum(row):
        ans = sum(row)
        sol = idx

print(sol)
