import sys
from collections import defaultdict, Counter


def get_pattern(s):
    i = 0
    d = {}
    pattern = []
    for c in s:
        if c not in d:
            d[c] = i
            i += 1
        pattern.append(d[c])

    return tuple(pattern)


N = int(sys.stdin.readline().rstrip())


dic = defaultdict(int)
words = [sys.stdin.readline().rstrip() for _ in range(N)]
patterns = [get_pattern(word) for word in words]

print(sum(map(lambda x: x * (x - 1) // 2, Counter(patterns).values())))
