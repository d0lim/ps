import sys

n = int(sys.stdin.readline().rstrip())
triangle = [[0, 0]]
triangle += [
    [0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0] for _ in range(n)
]

dp = [[0] * (i + 2) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n]))
