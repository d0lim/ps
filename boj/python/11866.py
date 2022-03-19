import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
q = deque([i for i in range(1, N + 1)])
res = []

while len(q) > 0:
    for _ in range(K - 1):
        q.append(q.popleft())
    res.append(q.popleft())

print('<' + ', '.join(map(str, res)) +'>')

