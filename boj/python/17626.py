import sys
from math import sqrt

n = int(sys.stdin.readline().rstrip())

squares = [i ** 2 for i in range(int(sqrt(n)))]

dp = [0] * 50001
dp[0] = 5
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    if sqrt(i).is_integer():
        dp[i] = 1
    else:
        m = []
        for s in squares:
            if s > i:
                break
            m.append(dp[s] + dp[i - s])
        dp[i] = min(m)

print(dp[n])
