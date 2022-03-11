import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
s = deque()
for _ in range(N):
    cmds = sys.stdin.readline().rstrip().split()
    if len(cmds) > 1:
        if cmds[0] == "push_front":
            s.appendleft(int(cmds[1]))
        else:
            s.append(int(cmds[1]))
    elif cmds[0] == "front":
        if len(s) > 0:
            print(s[0])
        else:
            print(-1)
    elif cmds[0] == "back":
        if len(s) > 0:
            print(s[-1])
        else:
            print(-1)
    elif cmds[0] == "pop_front":
        if len(s) > 0:
            print(s.popleft())
        else:
            print(-1)
    elif cmds[0] == "pop_back":
        if len(s) > 0:
            print(s.pop())
        else:
            print(-1)
    elif cmds[0] == "size":
        print(len(s))
    elif cmds[0] == "empty":
        print(1) if len(s) == 0 else print(0)
