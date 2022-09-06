from collections import deque

s = deque()

ps = list(input())

for p in ps:
    if p == "(":
        s.append(p)
    else:
        if s:
            top = s.pop()
            if top == "(":
                continue
            else:
                s.append(top)
                s.append(p)
        else:
            s.append(p)

print(len(s))
