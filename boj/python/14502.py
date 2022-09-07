import sys
from itertools import combinations
from collections import deque
from copy import deepcopy


def bfs(n, m, viruses, lab):
    q = deque()

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for virus_row, virus_col in viruses:
        q.append((virus_row, virus_col))

    while q:
        curr_row, curr_col = q.popleft()
        for dr, dc in dirs:
            next_row = curr_row + dr
            next_col = curr_col + dc
            if lab[next_row][next_col] == 0:
                q.append((next_row, next_col))
                lab[next_row][next_col] = 2

    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if lab[i][j] == 0:
                res += 1

    return res


N, M = map(int, sys.stdin.readline().rstrip().split())


lab = [[-1] * (M + 2)]
for _ in range(N):
    lab.append([-1] + list(map(int, sys.stdin.readline().rstrip().split())) + [-1])
lab += [[-1] * (M + 2)]

empties = []
viruses = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if lab[i][j] == 0:
            empties.append((i, j))
        elif lab[i][j] == 2:
            viruses.append((i, j))

combs = list(combinations(empties, 3))

final_result = 0
for comb in combs:
    copied_lab = deepcopy(lab)
    for row, col in comb:
        copied_lab[row][col] = 1

    res = bfs(N, M, viruses, copied_lab)
    if final_result < res:
        final_result = res

print(final_result)
