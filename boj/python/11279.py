import heapq, sys

N = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

heap = []

for num in nums:
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    heapq.heappush(heap, (-num, num))
