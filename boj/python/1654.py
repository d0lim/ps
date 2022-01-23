import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
k_arr = []
for _ in range(K):
    k_arr.append(int(sys.stdin.readline().rstrip()))

left = 1
right = max(k_arr)

while(left <= right):
    mid = (left + right) // 2
    cnt = 0
    for k in k_arr:
        cnt += k // mid
    
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1
    
print(right)