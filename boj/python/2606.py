import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

network = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    network[a].append(b)
    network[b].append(a)

visited = [False] * (n + 1)

q = deque()
q.append(1)
visited[1] = True
count = 0
while q:
    current = q.popleft()

    for next_computer in network[current]:
        if not visited[next_computer]:
            count += 1
            visited[next_computer] = True
            q.append(next_computer)

print(count)
