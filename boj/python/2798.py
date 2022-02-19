import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
combs = combinations(arr, 3)

result = 0
for comb in combs:
    comb_sum = sum(comb)
    result = comb_sum if M - comb_sum < M - result and comb_sum <= M else result

print(result)
