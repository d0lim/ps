import sys
from collections import defaultdict


N, D = map(int, input().split())

dp = [float("inf")] * 10001

fast = defaultdict(list)

for _ in range(N):
    s, e, l = map(int, sys.stdin.readline().rstrip().split())
    fast[e].append((s, l))

dp[0] = 0
for i in range(10001):
    for s, l in fast[i]:
        dp[i] = min(dp[i], dp[s] + l)
    dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[D])
