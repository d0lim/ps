from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    dic = {}
    comb = [0, 1, 2, 3]
    for i in info:
        person = i.split()
        conditions = person[:-1]
        score = int(person[-1])
        for j in range(5):
            for k in list(combinations(comb, j)):
                temp = conditions.copy()
                for idx in k:
                    temp[idx] = '-'
                key = ''.join(temp)
                if key in dic:
                    dic[key].append(score)
                else:
                    dic[key] = [score]
    # print(dic)
    for value in dic.values(): 
        value.sort()

    for q in query:
        q_list = q.split(' and ')
        q_list = q_list[:-1] + q_list[-1].split()

        target = int(q_list[-1])
        key = ''.join(q_list[:-1])

        if key in dic:
            score_list = dic[key]

            index = bisect_left(score_list, target)
            answer.append(len(score_list) - index)
        else:
            answer.append(0)
            continue
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))