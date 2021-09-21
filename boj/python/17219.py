import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

dic = {}

for _ in range(N):
    k, v = sys.stdin.readline().rstrip().split()
    dic[k] = v

for _ in range(M):
    print(dic[sys.stdin.readline().rstrip()])
