from collections import deque


origin = list(input())
bomb = list(input())

s = deque()
for c in origin:
    if c == bomb[-1]:
        t = deque()
        t.append(c)
        for b in reversed(bomb[:-1]):
            if s and s[-1] == b:
                t.append(s.pop())
            else:
                while t:
                    s.append(t.pop())
                break
    else:
        s.append(c)

print("".join(s) if s else "FRULA")
