import sys

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
        
    if str(N) == str(N)[::-1]:
        print('yes')
    else:
        print ('no')