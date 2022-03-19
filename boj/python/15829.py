import sys


def get_num(alphabet):
    return ord(alphabet) - 96


L = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

r = 31
M = 1234567891

res = 0
for i, c in enumerate(s):
    n = get_num(c)
    res = (res + n * (r**i)) % M
print(res)
