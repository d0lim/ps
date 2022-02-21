import sys
from collections import deque


while True:
    stack = deque()
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break

    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif c == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if len(stack) != 0:
            print("no")
        else:
            print("yes")
