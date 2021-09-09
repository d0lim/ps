from bisect import bisect_left
from collections import defaultdict
from itertools import combinations

def solution_crazy(info, query):
    answer = [0] * len(query)
    
    leaf = [[] for i in range(3 * 2 * 2 * 2)]
    for i in info:
        splitted_info = i.split()
        lang = splitted_info[0]
        job = splitted_info[1]
        career = splitted_info[2]
        food = splitted_info[3]
        test = int(splitted_info[4])
        if lang == 'cpp':
            if job == 'backend':
                if career == 'junior':
                    if food == 'chicken':
                        leaf[0].append(test)
                    else:
                        leaf[1].append(test)
                else:
                    if food == 'chicken':
                        leaf[2].append(test)
                    else:
                        leaf[3].append(test)
            else:
                if career == 'junior':
                    if food == 'chicken':
                        leaf[4].append(test)
                    else:
                        leaf[5].append(test)
                else:
                    if food == 'chicken':
                        leaf[6].append(test)
                    else:
                        leaf[7].append(test)
        elif lang == 'java':
            if job == 'backend':
                if career == 'junior':
                    if food == 'chicken':
                        leaf[8].append(test)
                    else:
                        leaf[9].append(test)
                else:
                    if food == 'chicken':
                        leaf[10].append(test)
                    else:
                        leaf[11].append(test)
            else:
                if career == 'junior':
                    if food == 'chicken':
                        leaf[12].append(test)
                    else:
                        leaf[13].append(test)
                else:
                    if food == 'chicken':
                        leaf[14].append(test)
                    else:
                        leaf[15].append(test)
        else:
            if job == 'backend':
                if career == 'junior':
                    if food == 'chicken':
                        leaf[16].append(test)
                    else:
                        leaf[17].append(test)
                else:
                    if food == 'chicken':
                        leaf[18].append(test)
                    else:
                        leaf[19].append(test)
            else:
                if career == 'junior':
                    if food == 'chicken':
                        leaf[20].append(test)
                    else:
                        leaf[21].append(test)
                else:
                    if food == 'chicken':
                        leaf[22].append(test)
                    else:
                        leaf[23].append(test)
    
    # print(leaf)
    for l in leaf:
        l.sort()

    for index, q in enumerate(query):
        splitted_query = q.split(' and ')
        splitted_query = splitted_query[:-1] + splitted_query[-1].split()
        q_lang = splitted_query[0]
        q_job = splitted_query[1]
        q_career = splitted_query[2]
        q_food = splitted_query[3]
        q_test = int(splitted_query[4])
        search_indices = []

        
        if q_lang == '-':
            if q_job == '-':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
                    elif q_food == 'chicken':
                        search_indices = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
                    else:
                        search_indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [0, 1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21]
                    elif q_food == 'chicken':
                        search_indices = [0, 4, 8, 12, 16, 20]
                    else:
                        search_indices = [1, 5, 9, 13, 17, 21]
                else:
                    if q_food == '-':
                        search_indices = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23]
                    elif q_food == 'chicken':
                        search_indices = [2, 6, 10, 14, 18, 22]
                    else:
                        search_indices = [3, 7, 11, 15, 19, 23]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [0, 1, 2, 3, 8, 9, 10, 11, 16, 17, 18, 19]
                    elif q_food == 'chicken':
                        search_indices = [0, 2, 8, 10, 16, 18]
                    else:
                        search_indices = [1, 3, 9, 11, 17, 19]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [0, 1, 8, 9, 16, 17]
                    elif q_food == 'chicken':
                        search_indices = [0, 8, 16]
                    else:
                        search_indices = [1, 9, 17]
                else:
                    if q_food == '-':
                        search_indices = [2, 3, 10, 11, 18, 19]
                    elif q_food == 'chicken':
                        search_indices = [2, 10, 18]
                    else:
                        search_indices = [3, 11, 19]
            else:
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23]
                    elif q_food == 'chicken':
                        search_indices = [4, 6, 12, 14, 20, 22]
                    else:
                        search_indices = [5, 7, 13, 15, 21, 23]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [4, 5, 12, 13, 20, 21]
                    elif q_food == 'chicken':
                        search_indices = [4, 12, 20]
                    else:
                        search_indices = [5, 13, 21]
                else:
                    if q_food == '-':
                        search_indices = [6, 7, 14, 15, 22, 23]
                    elif q_food == 'chicken':
                        search_indices = [6, 14, 22]
                    else:
                        search_indices = [7, 15, 23]
        elif q_lang == 'cpp':
            if q_job == '-':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [0, 1, 2, 3, 4, 5, 6, 7]
                    elif q_food == 'chicken':
                        search_indices = [0, 2, 4, 6]
                    else:
                        search_indices = [1, 3, 5, 7]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [0, 1, 4, 5]
                    elif q_food == 'chicken':
                        search_indices = [0, 4]
                    else:
                        search_indices = [1, 5]
                else:
                    if q_food == '-':
                        search_indices = [2, 3, 6, 7]
                    elif q_food == 'chicken':
                        search_indices = [2, 6]
                    else:
                        search_indices = [3, 7]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [0, 1, 2, 3]
                    elif q_food == 'chicken':
                        search_indices = [0, 2]
                    else:
                        search_indices = [1, 3]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [0, 1]
                    elif q_food == 'chicken':
                        search_indices = [0]
                    else:
                        search_indices = [1]
                else:
                    if q_food == '-':
                        search_indices = [2, 3]
                    elif q_food == 'chicken':
                        search_indices = [2]
                    else:
                        search_indices = [3]
            else:
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [4, 5, 6, 7]
                    elif q_food == 'chicken':
                        search_indices = [4, 6]
                    else:
                        search_indices = [5, 7]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [4, 5]
                    elif q_food == 'chicken':
                        search_indices = [4]
                    else:
                        search_indices = [5]
                else:
                    if q_food == '-':
                        search_indices = [6, 7]
                    elif q_food == 'chicken':
                        search_indices = [6]
                    else:
                        search_indices = [7]
        elif q_lang == 'java':
            if q_job == '-':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [8, 9, 10, 11, 12, 13, 14, 15]
                    elif q_food == 'chicken':
                        search_indices = [8, 10, 12, 14]
                    else:
                        search_indices = [9, 11, 13, 15]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [8, 9, 12, 13]
                    elif q_food == 'chicken':
                        search_indices = [8, 12]
                    else:
                        search_indices = [9, 13]
                else:
                    if q_food == '-':
                        search_indices = [10, 11, 14, 15]
                    elif q_food == 'chicken':
                        search_indices = [10, 14]
                    else:
                        search_indices = [11, 15]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [8, 9, 10, 11]
                    elif q_food == 'chicken':
                        search_indices = [8, 10]
                    else:
                        search_indices = [9, 11]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [8, 9]
                    elif q_food == 'chicken':
                        search_indices = [8]
                    else:
                        search_indices = [9]
                else:
                    if q_food == '-':
                        search_indices = [10, 11]
                    elif q_food == 'chicken':
                        search_indices = [10]
                    else:
                        search_indices = [11]
            else:
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [12, 13, 14, 15]
                    elif q_food == 'chicken':
                        search_indices = [12, 14]
                    else:
                        search_indices = [13, 15]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [12, 13]
                    elif q_food == 'chicken':
                        search_indices = [12]
                    else:
                        search_indices = [13]
                else:
                    if q_food == '-':
                        search_indices = [14, 15]
                    elif q_food == 'chicken':
                        search_indices = [14]
                    else:
                        search_indices = [15]
        else:
            if q_job == '-':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [16, 17, 18, 19, 20, 21, 22, 23]
                    elif q_food == 'chicken':
                        search_indices = [16, 18, 20, 22]
                    else:
                        search_indices = [17, 19, 21, 23]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [16, 17, 20, 21]
                    elif q_food == 'chicken':
                        search_indices = [16, 20]
                    else:
                        search_indices = [17, 21]
                else:
                    if q_food == '-':
                        search_indices = [18, 19, 22, 23]
                    elif q_food == 'chicken':
                        search_indices = [18, 22]
                    else:
                        search_indices = [19, 23]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [16, 17, 18, 19]
                    elif q_food == 'chicken':
                        search_indices = [16, 18]
                    else:
                        search_indices = [17, 19]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [16, 17]
                    elif q_food == 'chicken':
                        search_indices = [16]
                    else:
                        search_indices = [17]
                else:
                    if q_food == '-':
                        search_indices = [18, 19]
                    elif q_food == 'chicken':
                        search_indices = [18]
                    else:
                        search_indices = [19]
            else:
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [20, 21, 22, 23]
                    elif q_food == 'chicken':
                        search_indices = [20, 22]
                    else:
                        search_indices = [21, 23]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [20, 21]
                    elif q_food == 'chicken':
                        search_indices = [20]
                    else:
                        search_indices = [21]
                else:
                    if q_food == '-':
                        search_indices = [22, 23]
                    elif q_food == 'chicken':
                        search_indices = [22]
                    else:
                        search_indices = [23]
            
        # print(search_indices)
        
        
        passed = 0
        for search_index in search_indices:
            l = leaf[search_index]
            idx = bisect_left(l, q_test)
            passed += len(l) - idx
        answer[index] = passed
    
    return answer


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