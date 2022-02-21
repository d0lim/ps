import sys

while True:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if arr == [0, 0, 0]:
        break
    longest = max(arr)
    arr.pop(arr.index(longest))
    if longest ** 2 == arr[0] ** 2 + arr[1] ** 2:
        print("right")
    else:
        print("wrong")
