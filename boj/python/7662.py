import sys, heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    visited = [False] * 1000001
    i = 0
    max_heap = []
    min_heap = []

    for _ in range(k):
        c, n = sys.stdin.readline().rstrip().split()
        n = int(n)
        if c == "I":
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, n, i))
            visited[i] = True
        elif n == 1:
            while max_heap and not visited[max_heap[0][2]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][2]] = False
                heapq.heappop(max_heap)
        else:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
        i += 1

    while max_heap and not visited[max_heap[0][2]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if len(max_heap) == 0 or len(min_heap) == 0:
        print("EMPTY")
    else:
        print(
            " ".join(map(str, [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)[0]]))
        )
