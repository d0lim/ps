import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

dogam = {}

for i in range(N):
    pokemon = sys.stdin.readline().rstrip()
    dogam[str(i + 1)] = pokemon
    dogam[pokemon] = i + 1

for _ in range(M):
    query = sys.stdin.readline().rstrip()
    print(dogam[query])
