import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    stack = deque()
    ps = sys.stdin.readline().rstrip()
    for p in ps:
        if p == "(":
            stack.append("(")
        elif p == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")
