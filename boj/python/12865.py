import sys

N, K = map(int, input().split())
stuffs = []


dp = [[0] * (K + 1) for _ in range(N + 1)]
