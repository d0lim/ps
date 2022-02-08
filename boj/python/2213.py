from functools import reduce
import sys


N = int(sys.stdin.readline().rstrip())

for i in range(N):
    if i + reduce(lambda x, y: x + y, map(int, list(str(i)))) == N:
        print(i)
        break

else:
    print(0)
