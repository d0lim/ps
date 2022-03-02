import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())

q = deque()

for _ in range(K):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        q.pop()
    else:
        q.append(n)

print(sum(q))
