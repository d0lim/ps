from collections import defaultdict


def solution(id_list, report, k):
    reported = defaultdict(list)
    answer = defaultdict(int)
    for _id in id_list:
        reported[_id]
        answer[_id]

    for r in report:
        f, t = r.split()
        if f not in reported[t]:
            reported[t].append(f)

    for key, value in reported.items():
        if len(value) >= k:
            for u in value:
                answer[u] += 1

    return [answer[_id] for _id in id_list]


solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2,
)

solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
