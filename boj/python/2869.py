import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split())
day = (V - A) // (A - B)
remainder = (V - A) % (A - B)
print(day + 1) if remainder == 0 else print(day + 2)


# A*(day-1) - B*(day-1) + A >= V
# (day -1)(A - B) >= V - A
# day - 1 >= (V - A) // (A - B)
