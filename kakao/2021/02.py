from itertools import combinations
from collections import defaultdict, Counter


def filt(order, comb):
    flag = True
    for c in comb:
        if c not in order:
            flag = False
            break
    return flag


def solution(orders, course):
    s = set()
    l = 0
    combs = defaultdict(set)
    for order in map(list, orders):
        l = max(l, len(order))
        for o in order:
            s.add(o)

    for i in course:
        for order in map(list, orders):
            for comb in list(combinations(order, i)):
                combs[i].add(comb)

    print(combs)

    answer = []
    for co in course:
        max_cnt = 0
        tmp = []
        for comb in combs[co]:
            some = list(filter(lambda x: filt(x, comb), orders))
            cnt = len(some)
            if cnt >= 2:
                if cnt == max_cnt:
                    tmp.append("".join(comb))
                elif cnt > max_cnt:
                    max_cnt = cnt
                    tmp = ["".join(comb)]

        answer += tmp

    return list(sorted(answer))


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
