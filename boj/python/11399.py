import sys

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))
P.sort()
dp = [P[0]]
for i in range(1, len(P)):
    dp.append(P[i] + dp[i - 1])

print(sum(dp))
