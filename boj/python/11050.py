import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

K = N - K if N - K < K else K

res = 1
for i in range(N - K + 1, N + 1):
    res *= i
for i in range(1, K + 1):
    res //= i
print(res)
