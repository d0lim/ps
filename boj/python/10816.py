import sys

cards = [0] * 20000001
N = int(sys.stdin.readline().rstrip())
ns = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
fs = list(map(int, sys.stdin.readline().rstrip().split()))

for n in ns:
    cards[n + 10000000] += 1
print(" ".join(map(lambda x: str(cards[x + 10000000]), fs)))
