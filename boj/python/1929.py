from math import sqrt
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

e_che = [True for _ in range(N + 1)]
e_che[0] = False
e_che[1] = False
if M >= 2:
    e_che[2] = True
if M >= 3:
    e_che[3] = True
for i in range(4, N + 1):
    for j in range(2, int(sqrt(i) + 1)):
        if e_che[j] == False:
            continue
        elif i % j == 0:
            e_che[i] = False
            break
            

for i in range(M, N + 1):
    if e_che[i]:
        print(i)

