from collections import deque

def where(base_row, base_col, row, col, step):
    if row >= base_row:
        if col >= base_col:
            return 3, base_row + 2 ** step, base_col + 2 ** step
        else:
            return 2, base_row + 2 ** step, base_col - 2 ** step
    else:
        if col >= base_col:
            return 1, base_row - 2 ** step, base_col + 2 ** step
        else:
            return 0, base_row - 2 ** step, base_col - 2 ** step


[N, r, c] = list(map(int, input().split()))

deq = deque()
power = [4**i for i in range(N - 1, -1, -1)]

base_row = 2 ** (N - 1)
base_col = 2 ** (N - 1)
for i in range(N - 2, -2, -1):
    w, base_row, base_col = where(base_row, base_col, r, c, i)
    deq.append(w)
answer = 0
for p in power:
    answer += deq.popleft() * p
print(answer)