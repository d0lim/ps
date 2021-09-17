def print_paper(paper):
    for li in paper:
        print(li)

import sys
from copy import deepcopy

N = int(sys.stdin.readline().rstrip())

def modify_2d(paper, start_r, end_r, start_c, end_c, is_white):
    for i in range(start_r, end_r):
        for j in range(start_c, end_c):
            paper[i][j] = is_white
    return paper

def compare(paper, start_r, end_r, start_c, end_c, pattern):
    if [l[start_c:end_c] for l in paper[start_r:end_r]] == pattern:
        return True
    else:
        return False

paper = []

for _ in range(N):
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    paper.append(li)

paper_origin = deepcopy(paper)


pattern_blue = []
pattern_white = []
n = N
while n >= 1:
    pattern_blue.append([list([1]) * n for _ in range(n)])
    n //= 2
n = N
while n >= 1:
    pattern_white.append([list([0]) * n for _ in range(n)])
    n //= 2

count_blue = 0
n = N
for p in pattern_blue:
    pattern_length = len(p)
    for i in range(n // pattern_length):
        for j in range(n // pattern_length):
            if compare(paper, i * pattern_length, (i + 1) * pattern_length, j * pattern_length, (j + 1) * pattern_length, p):
                paper = modify_2d(paper, i * pattern_length, (i + 1) * pattern_length, j * pattern_length, (j + 1) * pattern_length, 0)
                count_blue += 1

paper = paper_origin
count_white = 0
for p in pattern_white:
    pattern_length = len(p)
    for i in range(n // pattern_length):
        for j in range(n // pattern_length):
            if compare(paper, i * pattern_length, (i + 1) * pattern_length, j * pattern_length, (j + 1) * pattern_length, p):
                paper = modify_2d(paper, i * pattern_length, (i + 1) * pattern_length, j * pattern_length, (j + 1) * pattern_length, 1)
                count_white += 1

print(count_white)
print(count_blue)
