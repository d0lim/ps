import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [100000] * 100002
dp[N] = 0
j = 1
for i in range(N - 1, -1, -1):
    dp[i] = j
    j += 1

for i in range(N + 1, 100001):
    if i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1], dp[i + 1]) + 1
    else:
        dp[i] = min(dp[i - 1], dp[i + 1]) + 1

for i in range(N + 1, 100001):
    if i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1], dp[i + 1]) + 1
    else:
        dp[i] = min(dp[i - 1], dp[i + 1]) + 1

print(dp[K])
