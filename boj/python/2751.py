import sys

N = int(sys.stdin.readline().rstrip())

arr = [False for _ in range(2000001)]

for _ in range(N):
    arr[int(sys.stdin.readline().rstrip()) + 1000000] = True

for i, v in enumerate(arr):
    if v:
        print(i - 1000000)
