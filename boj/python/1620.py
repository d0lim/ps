import sys
from collections import OrderedDict


N, M = map(int, (sys.stdin.readline().split()))

dic = OrderedDict()

for i in range(1, N + 1):
    info = sys.stdin.readline().rstrip('\n')
    dic[info] = i
    dic[str(i)] = info

for i in range(M):
    query = sys.stdin.readline().rstrip('\n')
    print(dic[query])