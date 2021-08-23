n = int(input())

dp = [1]

for i in range(1, n + 1):
    sol = 0
    for j in range(0, i):
        sol += dp[j] * dp[i - j - 1]
        # print("dp[", j, "]*dp[", i - j - 1, "]")
    dp.append(sol)

print(dp[n])
