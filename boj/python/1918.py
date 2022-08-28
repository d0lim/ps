import sys
from collections import deque

priority_score = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}

original = list(sys.stdin.readline().rstrip())


stack = deque()
ans = []


for c in original:
    if "A" <= c <= "Z":
        ans.append(c)
    elif c == "(":
        stack.append(c)
    elif c == ")":
        while stack and stack[-1] != "(":
            ans.append(stack.pop())
        stack.pop()
    else:
        while stack and priority_score[c] <= priority_score[stack[-1]]:
            ans.append(stack.pop())
        stack.append(c)

while stack:
    ans.append(stack.pop())

print("".join(ans))
