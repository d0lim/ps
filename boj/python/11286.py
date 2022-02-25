import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())

heap = []
for _ in range(N):
    cmd = int(sys.stdin.readline().rstrip())
    if cmd == 0:
        if len(heap) > 0:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, (abs(cmd), cmd))
