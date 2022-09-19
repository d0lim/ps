import sys

N = int(input())
strs = [sys.stdin.readline().rstrip() for _ in range(N)]
strs = list(sorted(strs, key=len))

res = 0
for i in range(len(strs)):
    is_prefix = False
    for j in range(i + 1, len(strs)):
        if strs[i] == strs[j][: len(strs[i])]:
            is_prefix = True
            break

    if not is_prefix:
        res += 1

print(res)
