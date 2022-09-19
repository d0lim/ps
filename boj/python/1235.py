import sys

N = int(input())

ids = [sys.stdin.readline().rstrip() for _ in range(N)]

len_ids = len(ids)
len_num = len(ids[0])

for i in range(len_num + 1):
    stripped = list(map(lambda x: x[len_num - i :], ids))
    len_set = len(set(stripped))
    if len_ids == len_set:
        print(i)
        break
