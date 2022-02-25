import sys
from collections import deque
from time import sleep

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())

    arr = [[] for _ in range(10000)]
    visited = [False for _ in range(10000)]

    # A -> B
    q = deque()
    q.append(A)
    visited[A] = True
    while len(q) > 0:
        curr = q.popleft()
        D = curr * 2 % 10000
        S = curr - 1 if curr != 0 else 9999
        L = curr % 1000 * 10 + curr // 1000
        R = curr % 10 * 1000 + curr // 10
        if not visited[D]:
            q.append(D)
            visited[D] = True
            arr[D] = arr[curr] + [0]
        if not visited[S]:
            q.append(S)
            visited[S] = True
            arr[S] = arr[curr] + [1]
        if not visited[L]:
            q.append(L)
            visited[L] = True
            arr[L] = arr[curr] + [2]
        if not visited[R]:
            q.append(R)
            visited[R] = True
            arr[R] = arr[curr] + [3]
        if B == D or B == S or B == L or B == R:
            break

    for k in arr[B]:
        if k == 0:
            sys.stdout.write("D")
        elif k == 1:
            sys.stdout.write("S")
        elif k == 2:
            sys.stdout.write("L")
        elif k == 3:
            sys.stdout.write("R")
    sys.stdout.write("\n")
