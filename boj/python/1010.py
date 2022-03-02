import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M, N = map(int, sys.stdin.readline().rstrip().split())
    M = N - M if N - M < M else M
    a = 1
    for i in range(M):
        a *= N - i
    b = 1
    for i in range(1, M + 1):
        b *= i
    print(a // b)
