from itertools import combinations_with_replacement


def check(apeach, ryan):
    apeach_score = 0
    ryan_score = 0
    for i in range(11):
        if not (apeach[i] == 0 and ryan[i] == 0):
            if apeach[i] >= ryan[i]:
                apeach_score += 10 - i
            else:
                ryan_score += 10 - i

    return ryan_score - apeach_score


def transform(comb):
    res = [0 for _ in range(11)]
    for n in comb:
        res[10 - n] += 1
    return res


def solution(n, info):
    combs = list(combinations_with_replacement([i for i in range(11)], n))
    ryans = [transform(comb) for comb in combs]

    res = 0
    answer = []
    for ryan in ryans:
        score_diff = check(info, ryan)

        if score_diff > res:
            res = score_diff
            answer = ryan

    return [-1] if not answer else answer


print(solution(2, [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# print(check([2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]))
