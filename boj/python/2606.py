import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

computers = [0] * (n + 1)
computers[1] = 1

link = []
for _ in range(m):
    link.append(tuple(sorted(map(int, (sys.stdin.readline().split())))))

link = sorted(link, key=lambda e: e[0])

for _ in range(m):
    for l in link:
        if computers[l[0]] == 1:
            computers[l[1]] = 1
        if computers[l[1]] == 1:
            computers[l[0]] = 1

print(computers.count(1) - 1)



