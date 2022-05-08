import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

aparts = [[0] * (N + 2)]
for _ in range(N):
    aparts.append([0] + list(map(int, list(sys.stdin.readline().rstrip()))) + [0])
aparts.append([0] * (N + 2))

visited = [[False for _ in range(N + 2)] for _ in range(N + 2)]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

section_count = 0
apart_counts = []
for row in range(1, N + 1):
    for col in range(1, N + 1):
        if not visited[row][col] and aparts[row][col] == 1:
            section_count += 1
            q = deque()
            q.append((row, col))
            visited[row][col] = True
            apart_count = 1
            while q:
                curr_row, curr_col = q.popleft()

                for dr, dc in dirs:
                    if (
                        not visited[curr_row + dr][curr_col + dc]
                        and aparts[curr_row + dr][curr_col + dc] == 1
                    ):
                        q.append((curr_row + dr, curr_col + dc))
                        visited[curr_row + dr][curr_col + dc] = True
                        apart_count += 1
            apart_counts.append(apart_count)

print(section_count)
for apart_count in sorted(apart_counts):
    print(apart_count)
