import sys

N = int(sys.stdin.readline().rstrip())
for t in list(
    sorted(
        map(
            lambda x: [int(x[0]), int(x[1])],
            [sys.stdin.readline().rstrip().split() for _ in range(N)],
        ),
        key=lambda x: (x[0], x[1]),
    )
):
    print(t[0], t[1])
