import sys
from itertools import permutations, combinations

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    original = list(sys.stdin.readline().rstrip())
    combs = list(
        sorted(
            map(lambda x: "".join(x), list(set(permutations(original, len(original)))))
        )
    )

    print(list(combinations(original, len(original))))

    print(
        combs[combs.index("".join(original)) + 1]
        if combs.index("".join(original)) < len(combs) - 1
        else "".join(original)
    )

# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
