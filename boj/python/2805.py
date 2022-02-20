import sys


def cut(h, trees):
    return sum(map(lambda x: x - h if x > h else 0, trees))


N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


# Binary Search
left = 0
right = max(arr)
result = 0

while left <= right:
    mid = (left + right) // 2
    after_cut = cut(mid, arr)

    if after_cut >= M:
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1


print(result)
