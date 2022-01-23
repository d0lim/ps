import sys

N = int(sys.stdin.readline().rstrip())

cnt = 0
i = 0
while cnt < N:
    if '666' in str(i):
        cnt += 1
    i += 1

print(i - 1)
    