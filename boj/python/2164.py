from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

cards = deque([i for i in range(1, N + 1)])
while len(cards) > 1:
    cards.popleft()
    top = cards.popleft()
    cards.append(top)
print(cards[0])
