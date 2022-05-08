import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().rstrip().split())

relations = defaultdict(list)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    relations[A].append(B)
    relations[B].append(A)

result = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    q = deque()
    q.append(i)
    visited[i] = True
    count = [0] * (N + 1)
    while q:
        current = q.popleft()

        for friend in relations[current]:
            if not visited[friend]:
                q.append(friend)
                visited[friend] = True
                count[friend] = count[current] + 1

    result.append(sum(count))

insider = 0
insider_value = result[0]
for i, v in enumerate(result):
    if v < insider_value:
        insider = i
        insider_value = v

print(insider + 1)
