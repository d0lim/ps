import sys

N, M = map(int, (sys.stdin.readline().split()))

no_heard  = set()
no_seen = set()

for _ in range(N):
    no_heard.add(sys.stdin.readline().rstrip())
for _ in range(M):
    no_seen.add(sys.stdin.readline().rstrip())

dbj = sorted(list(no_heard & no_seen))
print(len(dbj))
for p in dbj:
    print(p)


