def calcul_rate(x, y, n):
    return int((y + n) * 100 // (x + n))


X, Y = map(int, input().split())

rate = calcul_rate(X, Y, 0)

l, r = 1, X

res = float("inf")
while l <= r:
    m = (l + r) // 2
    curr_rate = calcul_rate(X, Y, m)

    if rate < curr_rate:
        res = min(res, m)
        r = m - 1
    else:
        l = m + 1

print(res if res != float("inf") else -1)
