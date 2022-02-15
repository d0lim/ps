import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    i = int(sys.stdin.readline().rstrip())

    dp = [
        list([0 for _ in range(i + 1)]) if f != 0 else list([r for r in range(i + 1)])
        for f in range(k + 1)
    ]

    for l in range(1, k + 1):
        for j in range(1, i + 1):
            dp[l][j] = sum(dp[l - 1][1 : j + 1])

    print(dp[k][i])
