import sys
from collections import defaultdict


dic = defaultdict(int)

s = list(input())
for c in s:
    dic[c] += 1

res_diagonal = []

for k in sorted(dic.keys()):
    first_count = dic[k] // 2
    for _ in range(first_count):
        res_diagonal.append(k)
    dic[k] -= (dic[k] // 2) * 2

cnt = 0
res_center = ""
for k, v in dic.items():
    if v >= 1:
        cnt += 1
    if v == 1:
        res_center = k

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print("".join([*res_diagonal, res_center, *reversed(res_diagonal)]))
