import sys
from collections import deque

N, M = map(int, input().split())

matrix = [[-1 for _ in range(M + 2)]]
matrix += [
    [-1] + list(map(int, list(sys.stdin.readline().rstrip()))) + [-1] for _ in range(N)
]
matrix += [[-1 for _ in range(M + 2)]]

final_result = []

q = deque()
visited = [[[float("inf")] * (M + 2) for _ in range(N + 2)] for _ in range(2)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q.append((1, 1, 1, False))
visited[0][1][1] = 1

result_cost = float("inf")
while q:
    curr_x, curr_y, cost, skipped = q.popleft()

    if curr_x == N and curr_y == M:
        result_cost = min(cost, result_cost)
    for dx, dy in dirs:
        if (
            matrix[curr_x + dx][curr_y + dy] == 0
            and skipped
            and visited[1][curr_x + dx][curr_y + dy] > cost + 1
        ):
            visited[1][curr_x + dx][curr_y + dy] = cost + 1
            q.append((curr_x + dx, curr_y + dy, cost + 1, skipped))
        if (
            matrix[curr_x + dx][curr_y + dy] == 0
            and not skipped
            and visited[0][curr_x + dx][curr_y + dy] > cost + 1
        ):
            visited[0][curr_x + dx][curr_y + dy] = cost + 1
            q.append((curr_x + dx, curr_y + dy, cost + 1, skipped))
        if (
            matrix[curr_x + dx][curr_y + dy] == 1
            and not skipped
            and visited[1][curr_x + dx][curr_y + dy] > cost + 1
        ):
            visited[1][curr_x + dx][curr_y + dy] = cost + 1
            q.append((curr_x + dx, curr_y + dy, cost + 1, True))

if visited[0][N][M] != float("inf") or visited[1][N][M] != float("inf"):
    final_result.append(result_cost)


print(min(final_result) if final_result else -1)
