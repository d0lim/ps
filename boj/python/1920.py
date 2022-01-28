import sys

N = int(sys.stdin.readline().rstrip())
input_arr = list(map(int, sys.stdin.readline().rstrip().split()))

n_set = set()
for i in input_arr:
    n_set.add(i)
M = int(sys.stdin.readline().rstrip())
test_arr = list(map(int, sys.stdin.readline().rstrip().split()))
for t in test_arr:
    if t in n_set:
        print(1)
    else:
        print(0)
