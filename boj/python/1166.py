N, L, W, H = map(int, input().split())
l, r = 0, max(L, W, H)

for _ in range(150):
    m = (l + r) / 2
    if (L // m) * (W // m) * (H // m) < N:
        r = m
    else:
        l = m


print("%.10f" % (r))
