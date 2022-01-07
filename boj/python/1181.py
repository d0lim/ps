import sys

N = int(sys.stdin.readline().rstrip())

str_set = set()
for _ in range(N):
    str_set.add(sys.stdin.readline().rstrip())

sorted_arr = list(sorted(str_set, key=lambda x: (len(x), x)))

for s in sorted_arr:
    print(s)