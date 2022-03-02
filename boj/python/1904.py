import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * 1000002
dp[1] = 1

for i in range(2, N + 2):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N + 1])
