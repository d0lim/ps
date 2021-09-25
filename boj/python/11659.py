import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

i_list = list(map(int, sys.stdin.readline().rstrip().split()))
s_list = [0]

for idx, l in enumerate(i_list):
    if idx == 0:
        s_list.append(l)
    else:
        s_list.append(l + s_list[idx])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(s_list[j] - s_list[i - 1])
