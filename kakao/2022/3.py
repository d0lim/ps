def apply_skill(acc, skill):
    t, r1, c1, r2, c2, degree = skill
    degree = -1 * degree if t == 1 else degree

    acc[r1][c1] += degree
    if c2 < len(acc[0]) - 1:
        acc[r1][c2 + 1] += -1 * degree
    if r2 < len(acc) - 1:
        acc[r2 + 1][c1] += -1 * degree
    if c2 < len(acc[0]) - 1 and r2 < len(acc) - 1:
        acc[r2 + 1][c2 + 1] += degree

    return acc


def solution(board, skill):
    acc = [[0] * len(board[0]) for _ in range(len(board))]

    for s in skill:
        acc = apply_skill(acc, s)

    for j in range(1, len(acc[0])):
        acc[0][j] = acc[0][j] + acc[0][j - 1]
    for i in range(1, len(acc)):
        acc[i][0] = acc[i][0] + acc[i - 1][0]
    for i in range(1, len(acc)):
        for j in range(1, len(acc[0])):
            acc[i][j] = acc[i][j] + acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1]

    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + acc[i][j] > 0:
                cnt += 1

    return cnt


print(
    solution(
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [
            [1, 0, 0, 3, 4, 4],
            [1, 2, 0, 2, 3, 2],
            [2, 1, 0, 3, 1, 2],
            [1, 0, 1, 3, 3, 1],
        ],
    )
)
