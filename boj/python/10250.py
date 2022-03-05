import sys


def convert_s(s):
    if len(s) == 1:
        return "0" + s
    return s


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    x = (N - 1) // H + 1
    y = (N - 1) % H + 1

    s_x = str(x)
    s_y = str(y)
    print(s_y + convert_s(s_x))
