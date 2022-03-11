import sys

l = [0] * 10001

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    l[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(l)):
    if l[i] != 0:
        for j in range(l[i]):
            print(i)
