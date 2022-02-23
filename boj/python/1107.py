import sys


def check(num):
    num = list(str(num))
    for i in num:
        if i in s:
            return False
    return True


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
s = list(sys.stdin.readline().rstrip().split())
result = abs(n - 100)
for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i - n))
print(result)
