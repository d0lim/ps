from collections import deque
import sys
import copy


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    field = [[False for _ in range(N + 2)] for _ in range(M + 2)]
    visited = copy.deepcopy(field)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(K):
        cabbage_row, cabbage_col = map(int, sys.stdin.readline().rstrip().split())
        field[cabbage_row + 1][cabbage_col + 1] = True

    count = 0
    for m in range(1, M + 2):
        for n in range(1, N + 2):
            if field[m][n] == True and visited[m][n] == False:
                q = deque()
                q.append((m, n))
                visited[m][n] = True
                while len(q) > 0:
                    row, col = q.popleft()

                    # Check up, down, right, left
                    for a, b in direction:
                        if field[row + a][col + b] and not visited[row + a][col + b]:
                            visited[row + a][col + b] = True
                            q.append((row + a, col + b))

                count += 1

    print(count)
