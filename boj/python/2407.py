from functools import reduce


n, m = map(int, input().split())

if m > n // 2:
    m = n - m

top = [n - i for i in range(m)]
bottom = [i for i in range(1, m + 1)]

top_mult = reduce(lambda acc, curr: acc * curr, top)
bottom_mult = reduce(lambda acc, curr: acc * curr, bottom)

print(top_mult // bottom_mult)
