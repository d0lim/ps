import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    done = False
    while x <= M * N:
        if (x - y) % N == 0:
            done = True
            print(x)
            break
        x += M
    if not done:
        print(-1)
