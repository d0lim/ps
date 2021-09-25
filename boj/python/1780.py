import sys


def print_paper(paper):
    for row in paper:
        print(row)


def check(paper):
    default = paper[0][0]
    for row in paper:
        for col in row:
            if col != default:
                return -2
    else:
        return default


def slice_2d_by_3(paper, start_row, start_col):
    return list(
        map(
            lambda r: r[start_col : start_col + len(paper) // 3],
            paper[start_row : start_row + len(paper) // 3],
        )
    )


def sol(paper):
    minuses = 0
    zeros = 0
    ones = 0
    c = check(paper)
    l = len(paper) // 3
    if c != -2:
        if c == 1:
            return 0, 0, 1
        elif c == 0:
            return 0, 1, 0
        else:
            return 1, 0, 0
    else:
        for i in range(3):
            for j in range(3):
                m, z, o = sol(slice_2d_by_3(paper, i * l, j * l))
                minuses += m
                zeros += z
                ones += o
        return minuses, zeros, ones


N = int(sys.stdin.readline().rstrip())

paper = []

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))


a, b, c = sol(paper)
print(a)
print(b)
print(c)
