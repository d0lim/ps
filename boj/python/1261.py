import sys
from collections import deque


M, N = map(int, sys.stdin.readline().rstrip().split())

maze = [[0] * (M + 2)]
for _ in range(N):
    maze.append([0] + list(map(int, list(sys.stdin.readline().rstrip()))) + [0])
maze.append([0] * (M + 2))


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = [[-1] * (M + 2) for _ in range(N + 2)]

q = deque()
q.append((1, 1))
visited[1][1] = 0
while q:
    curr_r, curr_c = q.popleft()
    if curr_r == N and curr_c == M:
        break
    for dr, dc in dirs:
        next_r, next_c = curr_r + dr, curr_c + dc
        if visited[next_r][next_c] == -1 and 0 < next_r <= N and 0 < next_c <= M:
            if maze[next_r][next_c] == 0:
                visited[next_r][next_c] = visited[curr_r][curr_c]
                q.appendleft((next_r, next_c))
            else:
                visited[next_r][next_c] = visited[curr_r][curr_c] + 1
                q.append((next_r, next_c))

print(visited[N][M])
