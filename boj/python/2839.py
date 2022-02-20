import sys

N = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(5001)]

dp[1] = -1
dp[2] = -1
dp[3] = 1
dp[4] = -1
dp[5] = 1
for i in range(6, N + 1):
    before_3 = dp[i - 3]
    before_5 = dp[i - 5]
    if before_3 == -1 and before_5 == -1:
        dp[i] = -1
        continue
    else:
        if before_3 == -1:
            dp[i] = before_5 + 1
        elif before_5 == -1:
            dp[i] = before_3 + 1
        else:
            dp[i] = before_3 + 1 if before_3 < before_5 else before_5 + 1


print(dp[N])
