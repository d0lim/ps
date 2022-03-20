import sys

N, M, B = map(int, sys.stdin.readline().rstrip().split())

field = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

minimal_time = sys.maxsize
height = 0
for i in range(257):
    # i 개로 맞춰버릴 것
    blocks = B
    available = True
    temp_time = 0
    for j in range(N):
        for k in range(M):
            # 계산을 해야한다.
            # 파내야 하는 경우
            curr = field[j][k]
            if i < curr:
                temp_time += (curr - i) * 2
                blocks += curr - i
            # 메워야 하는 경우
            elif i > curr:
                temp_time += i - curr
                blocks -= i - curr
                # if blocks < 0:
                #     available = False
    if blocks < 0:
        continue
    if minimal_time >= temp_time:
        minimal_time = temp_time
        height = i


print(minimal_time, height)
