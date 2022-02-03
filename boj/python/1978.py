import sys

nums = [True for _ in range(1001)]

nums[0] = False
nums[1] = False
# e-che
for i in range(2, int(1001 ** 0.5) + 1):
    if nums[i]:
        m = 1001 // i
        if m * i < 1001:
            m += 1
        for j in range(2, m):
            nums[i * j] = False

N = int(sys.stdin.readline().rstrip())
T = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
for t in T:
    if nums[t]:
        cnt += 1

print(cnt)