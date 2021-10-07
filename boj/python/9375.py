import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    dic = {}
    m = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        _, category = sys.stdin.readline().rstrip().split()
        dic.setdefault(category, 0)
        dic[category] += 1
    count = 1
    for v in dic.values():
        count *= v + 1
    print(count - 1)
