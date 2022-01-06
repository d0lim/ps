import sys

def printM(m):
    for i in range(N):
        print(m[i])

def compare_with_answer(m, start_x, start_y):
    ansB = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
    ]
    ansW = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
    ]
    count_w = 0
    count_b = 0
    for i in range(8):
        for j in range(8):
            if m[start_x + i][start_y + j] != ansB[i][j]:
                count_b += 1
    for i in range(8):
        for j in range(8):
            if m[start_x + i][start_y + j] != ansW[i][j]:
                count_w += 1
    count = count_w if count_w < count_b else count_b
    return count

N, M = map(int, sys.stdin.readline().rstrip().split())



matrix = [[0] * (M) for _ in range(N)]

for i in range(N):
    s = list(sys.stdin.readline().rstrip())
    for (j, c) in enumerate(s):
        matrix[i][j] = 1 if c == 'B' else 0

cnt = 99999999999
for i in range(N - 7):
    for j in range(M - 7):
        c = compare_with_answer(matrix, i, j)
        cnt = c if c < cnt else cnt
    
print(cnt)



