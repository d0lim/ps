def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        dic[c] -= 1
    for k, d in dic.items():
        if d != 0:
            return k

import collections

## Counter를 이용한 풀이
def solution_good(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]