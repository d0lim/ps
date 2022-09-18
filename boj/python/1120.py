A, B = input().split()

la = len(A)
lb = len(B)

d = lb - la
res = float("inf")
for i in range(d + 1):
    cnt = 0
    for a, b in zip(A, B[i : i + la]):
        if a != b:
            cnt += 1
    res = min(res, cnt)

print(res)
