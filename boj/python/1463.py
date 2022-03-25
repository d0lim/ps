import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * 1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1


for i in range(4, N + 1):
    temp = []
    if i % 3 == 0:
        temp.append(dp[i // 3])
    if i % 2 == 0:
        temp.append(dp[i // 2])
    temp.append(dp[i - 1])
    dp[i] = min(temp) + 1

print(dp[N])
