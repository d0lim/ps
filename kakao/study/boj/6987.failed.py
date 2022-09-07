import sys
from collections import defaultdict

cases = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(4)]

for case in cases:
    # 일단, 3개 합이 다 6이어야함
    good = True
    for i in range(6):
        if sum(case[i * 3 : i * 3 + 3]) != 5:
            good = False
            break

    # 그리고, 승의 합이 패의 합과 같아야 함
    if good:
        win = 0
        lose = 0
        draw = 0
        draw_map = defaultdict(int)
        draw_team_count = 0
        for i in range(6):
            win += case[i * 3]
            # print("win", case[i * 3])
            draw += case[i * 3 + 1]
            if case[i * 3 + 1] != 0:
                draw_map[case[i * 3 + 1]] += 1
                draw_team_count += 1
            lose += case[i * 3 + 2]
            # print("lose", case[i * 3 + 2])
        if win != lose:
            good = False

        if good:
            # 그리고, 무승부가 분배되어 있어야 함
            if draw_team_count == 1:

                good = False
            if sum(draw_map.values()) % 2 != 0:
                good = False
            # for v in draw_map.values():
            #     if v % 2 != 0:
            #         good = False
            #         break

    print("1" if good else "0", end=" ")
print()
