import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

ladder = dict()
snake = dict()

for _ in range(N):
    ladder_start, ladder_end = map(int, sys.stdin.readline().rstrip().split())
    ladder[ladder_start] = ladder_end

for _ in range(M):
    snake_start, snake_end = map(int, sys.stdin.readline().rstrip().split())
    snake[snake_start] = snake_end

q = deque()
arr = [0 for _ in range(101)]
visited = [False for _ in range(101)]

q.append(1)
visited[1] = True
dice = [1, 2, 3, 4, 5, 6]

while len(q) > 0:
    index = q.popleft()
    for k in dice:
        next_index = index + k
        if 1 <= next_index <= 100:
            if next_index in ladder.keys():
                next_index = ladder[next_index]
            if next_index in snake:
                next_index = snake[next_index]
            if not visited[next_index]:
                q.append(next_index)
                visited[next_index] = True
                arr[next_index] = arr[index] + 1
print(arr[100])
