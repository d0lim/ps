import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
max_coin = max(coins)
dp = [0] * (k + 1)
for coin in coins:
    for i in range(1, k + 1):
        if coin == i:
            dp[i] += 1
        elif i > coin:
            dp[i] += dp[i - coin]

print(dp[k])
