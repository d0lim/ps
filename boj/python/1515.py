import sys
from collections import deque

n_q = deque(list(input()))
i = 1
s = ""
while True:
    s += str(i)
    done = True
    while n_q:
        n = n_q.popleft()
        if n in s:
            idx = s.index(n)
            s = s[idx + 1 :]

        else:
            done = False
            n_q.appendleft(n)
            break

    if done:
        print(i)
        break
    i += 1
