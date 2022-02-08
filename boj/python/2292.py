import sys

N = int(sys.stdin.readline().rstrip())

count = 0
last = 1
while last + 6 * count < N:
    last += 6 * count
    count += 1


print(count + 1)
