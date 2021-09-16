from collections import deque

def print_field(field):
    for row in field:
        print(row)

T = int(input())
for i in range(T):
    test_info = input().split()
    M = int(test_info[0])
    N = int(test_info[1])
    K = int(test_info[2])
    print('INFO', M, N, K)
    field = [list([0] * N) for j in range(M)]
    worm = [list([0] * N) for j in range(M)]
    for j in range(K):
        cabbage = input().split()
        field[int(cabbage[0])][int(cabbage[1])] = 1
    print("---------- Initial Field -----------")
    print_field(field)
    print("------------------------------------")
    
    count = 0
    for m in range(M):
        for n in range(N):
            if field[m][n] == 1:
                if worm[m][n] == 0:
                    worm_m = m
                    worm_n = n
                    worm[m][n] = 1
                    # 상하좌우 BFS 탐색 시작
                    q = deque()
                    while True:
                        if len(q) > 0:
                            worm_m, worm_n = q.popleft()
                        if worm_m < M - 1 and field[worm_m + 1][worm_n] == 1 and worm[worm_m + 1][worm_n] == 0:
                            worm[worm_m + 1][worm_n] = 1
                            q.append((worm_m + 1, worm_n))
                        if worm_m > 0 and field[worm_m - 1][worm_n] == 1 and worm[worm_m - 1][worm_n] == 0:
                            worm[worm_m - 1][worm_n] = 1
                            q.append((worm_m - 1, worm_n))
                        if worm_n < N - 1 and field[worm_m][worm_n + 1] == 1 and worm[worm_m][worm_n + 1] == 0:
                            worm[worm_m][worm_n + 1] = 1
                            q.append((worm_m, worm_n + 1))
                        if worm_n > 0 and field[worm_m][worm_n - 1] == 1 and worm[worm_m][worm_n - 1] == 0:
                            worm[worm_m][worm_n - 1] = 1
                            q.append((worm_m, worm_n - 1))
                        # print(q)
                        if len(q) == 0:
                            count += 1
                            break

    print("---------- After Field -------------")
    print_field(field)
    print("------------------------------------")
    print("------------ After Worm ------------")
    print_field(field)
    print("------------------------------------")
    print("COUNT:", count)