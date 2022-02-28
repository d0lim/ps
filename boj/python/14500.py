import sys


def dfs(p, v, row, col, c, n):
    global result
    v[row][col] = True
    n += p[row][col]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if c == 3:
        result = max(result, n)
    else:
        for a, b in directions:
            if not v[row + a][col + b] and not p[row + a][col + b] == 0 and c < 3:
                dfs(p, v, row + a, col + b, c + 1, n)
    v[row][col] = False


def check_o(p, row, col):
    global result

    o_shapes = [
        [[0, 1, 0], [1, 1, 1]],
        [[1, 1, 1], [0, 1, 0]],
        [[1, 0], [1, 1], [1, 0]],
        [[0, 1], [1, 1], [0, 1]],
    ]

    for o_shape in o_shapes:
        temp = 0
        edge = False
        # upper 2 rows
        if len(o_shape) == 2:
            for i in range(2):
                for j in range(3):
                    if p[row + i][col + j] == 0:
                        edge = True
                    temp += o_shape[i][j] * p[row + i][col + j]
        # next 2 rows
        else:
            for i in range(3):
                for j in range(2):
                    if p[row + i][col + j] == 0:
                        edge = True
                    temp += o_shape[i][j] * p[row + i][col + j]
        if not edge:
            result = max(result, temp)


N, M = map(int, sys.stdin.readline().rstrip().split())
paper = [[0] * (M + 2)]
paper += [
    [0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0] for _ in range(N)
]
paper += [[0] * (M + 2)]


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = 0
visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]

for row in range(1, N + 1):
    for col in range(1, M + 1):
        dfs(paper, visited, row, col, 0, 0)
        if row < N and col < M:
            check_o(paper, row, col)

print(result)
