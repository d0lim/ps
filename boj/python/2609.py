import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

gcd = 0
lcm = 99999

a, b = (N, M) if N > M else (M, N)

while True:
    mod = a % b
    if mod == 0:
        gcd = b
        lcm = N * M // b
        break
    a = b
    b = mod

print(gcd)
print(lcm)
