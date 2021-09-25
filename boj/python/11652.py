import sys
from collections import OrderedDict

N = int(sys.stdin.readline().rstrip())

dic = {}

for _ in range(N):
    i = int(sys.stdin.readline().rstrip())
    dic.setdefault(i, 0)
    dic[i] += 1

ordered = OrderedDict(sorted(dic.items(), key=lambda e: (-e[1], e[0])))
print(list(ordered.keys())[0])
