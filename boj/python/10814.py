import sys

N = int(sys.stdin.readline().rstrip())
for age, name, _ in sorted(
    map(
        lambda x: (int(x[0]), x[1], x[2]),
        [sys.stdin.readline().rstrip().split() + [i] for i in range(N)],
    ),
    key=lambda x: (x[0], x[2]),
):
    print(age, name)
