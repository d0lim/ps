import sys

N = int(sys.stdin.readline().rstrip())

sessions = []
for _ in range(N):
    sessions.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

sessions = sorted(sessions, key=lambda e: (e[1], e[0]))

m = 0
c = 0
for session in sessions:
    if session[0] >= m:
        c += 1
        m = session[1]

print(c)