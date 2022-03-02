import sys

n = int(sys.stdin.readline().rstrip())

fib = [0] * 91
fib[1] = 1
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

print(fib[n])
