import sys

T = int(sys.stdin.readline().rstrip())

dp = [
    list([0 for _ in range(15)]) if f != 0 else list([r for r in range(15)])
    for f in range(15)
]

for l in range(1, 15):
    for j in range(1, 15):
        dp[l][j] = sum(dp[l - 1][1 : j + 1])

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    i = int(sys.stdin.readline().rstrip())

    print(dp[k][i])
