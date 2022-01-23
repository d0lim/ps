import sys

n = int(sys.stdin.readline().rstrip())

stack = []
seq = []
for _ in range(n):
    seq.append(int(sys.stdin.readline().rstrip()))

j = 0
res = []
for i in range(1, n + 1):
    while len(stack) > 0 and stack[0] == seq[j]:
        if len(stack) != 0:
            r = stack.pop(0)
            j += 1
            res.append('-')
    else:
        stack.insert(0, i)
        res.append('+')

while len(stack) > 0 and stack[0] == seq[j]:
    if len(stack) != 0:
        r = stack.pop(0)
        j += 1
        res.append('-')

if len(stack) > 0:
    print('NO')
else:
    for c in res:
        print(c)