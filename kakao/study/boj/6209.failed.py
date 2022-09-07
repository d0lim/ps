import sys

d, n, m = map(int, sys.stdin.readline().rstrip().split())

rocks = list(sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)]))

result = 0


# for comb in combs:
#     temp = comb[0]
#     for i in range(n - m - 1):
#         if comb[i + 1] - comb[i] < temp:
#             temp = comb[i + 1] - comb[i]
#     if d - comb[-1] < temp:
#         temp = d - comb[-1]
#     if result < temp:
#         result = temp

# print(result)
