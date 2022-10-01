import sys

N, M = map(int, input().split())

field = list(map(int, sys.stdin.readline().rstrip().split()))

acc = [0 for _ in range(N)]

for _ in range(M):
    a, b, k = map(int, sys.stdin.readline().rstrip().split())
    acc[a - 1] += k
    if b < N:
        acc[b] -= k

for i in range(1, N):
    acc[i] = acc[i] + acc[i - 1]

for i in range(N):
    field[i] += acc[i]

print(" ".join(map(str, field)))
