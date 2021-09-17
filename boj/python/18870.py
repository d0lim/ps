import sys

N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().rstrip().split()))

I = [i for i in range(N)]
zipped = list(map(list, zip(I, X)))
s = sorted(zipped, key=lambda e: e[1])

count = -1
m = -10e9 - 1
for z in s:
    if z[1] > m:
        m = z[1]
        count += 1
    z.append(count)

s = sorted(zipped, key=lambda e: e[0])

print(" ".join(map(lambda e: str(e[2]), s)))
