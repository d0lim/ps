import sys
from collections import deque

q = deque()

N, K = map(int, input().split())

points = [float("inf")] * 100001

q.append((N, 0))
points[N] = 0

res = float("inf")
cnt = 0

while q:
    curr, val = q.popleft()
    if curr == K:
        if val < res:
            res = val
            cnt = 1
        elif val == res:
            cnt += 1

    # +1
    if curr + 1 <= 100000 and points[curr + 1] >= val + 1:
        points[curr + 1] = val + 1
        q.append((curr + 1, val + 1))
    if curr - 1 >= 0 and points[curr - 1] >= val + 1:
        points[curr - 1] = val + 1
        q.append((curr - 1, val + 1))
    if curr * 2 <= 100000 and points[curr * 2] >= val + 1:
        points[curr * 2] = val + 1
        q.append((curr * 2, val + 1))


print(res)
print(cnt)
