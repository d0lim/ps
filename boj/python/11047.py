import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

price = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

count = 0
for p in reversed(price):
    if K != 0:
        d = K // p
        count += d
        K = K - d * p
    else:
        break

print(count)
