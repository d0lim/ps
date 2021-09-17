import sys

M = int(sys.stdin.readline())

s = set()

for i in range(M):
    command = sys.stdin.readline().split()
    c = command[0]
    if len(command) > 1:
        n = int(command[1])
    if c == 'add':
        s.add(n)
    elif c == 'remove':
        try:
            s.remove(n)
        except:
            pass
    elif c == 'check':
        if n in s:
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        if n in s:
            try:
                s.remove(n)
            except:
                pass
        else:
            s.add(n)
    elif c == 'all':
        s = set([j for j in range(1, 21)])
    else:
        s = set()