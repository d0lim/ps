

def solution(info, query):
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
                        search_indices = [i for i in range(24)]
                    elif q_food == 'chicken':
                        search_indices = [i for i in range(24) if i % 2 == 0]
                    else:
                        search_indices = [i for i in range(24) if i % 2 == 1]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [i * 4 for i in range(6)] + [i * 4 + 1 for i in range(6)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 for i in range(6)]
                    else:
                        search_indices = [i * 4 + 1 for i in range(6)]
                else:
                    if q_food == '-':
                        search_indices = [i * 4 + 2 for i in range(6)] + [i * 4 + 3 for i in range(6)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 + 2 for i in range(6)]
                    else:
                        search_indices = [i * 4 + 3 for i in range(6)]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8, i * 8 + 4)]
                    elif q_food == 'chicken':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8, i * 8 + 4) if j % 2 == 0]
                    else:
                        search_indices = [j for i in range(0, 3) for j in range(i * 8, i * 8 + 4) if j % 2 == 1]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8, i * 8 + 2)]
                    elif q_food == 'chicken':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8, i * 8 + 2) if j % 2 == 0]
                    else:
                        search_indices = [j for i in range(0, 3) for j in range(i * 8, i * 8 + 2) if j % 2 == 1]
                else:
                    if q_food == '-':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 2, i * 8 + 4)]
                    elif q_food == 'chicken':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 2, i * 8 + 4) if j % 2 == 0]
                    else:
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 2, i * 8 + 4) if j % 2 == 1]
            else:
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 4, i * 8 + 8)]
                    elif q_food == 'chicken':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 4, i * 8 + 8) if j % 2 == 0]
                    else:
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 4, i * 8 + 8) if j % 2 == 1]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 4, i * 8 + 6)]
                    elif q_food == 'chicken':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 4, i * 8 + 6) if j % 2 == 0]
                    else:
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 4, i * 8 + 6) if j % 2 == 1]
                else:
                    if q_food == '-':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 6, i * 8 + 8)]
                    elif q_food == 'chicken':
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 6, i * 8 + 8) if j % 2 == 0]
                    else:
                        search_indices = [j for i in range(0, 3) for j in range(i * 8 + 6, i * 8 + 8) if j % 2 == 1]
        elif q_lang == 'cpp':
            if q_job == '-':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [i for i in range(8)]
                    elif q_food == 'chicken':
                        search_indices = [i * 2 for i in range(4)]
                    else:
                        search_indices = [i * 2 + 1 for i in range(4)]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [i * 4 for i in range(2)] + [i * 4 + 1 for i in range(2)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 for i in range(2)]
                    else:
                        search_indices = [i * 4 + 1 for i in range(2)]
                else:
                    if q_food == '-':
                        search_indices = [i * 4 + 2 for i in range(2)] + [i * 4 + 3 for i in range(2)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 + 2 for i in range(2)]
                    else:
                        search_indices = [i * 4 + 3 for i in range(2)]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [i for i in range(4)]
                    elif q_food == 'chicken':
                        search_indices = [i for i in range(4) if i % 2 == 0]
                    else:
                        search_indices = [i for i in range(4) if i % 2 == 1]
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
                        search_indices = [i for i in range(4, 8)]
                    elif q_food == 'chicken':
                        search_indices = [i for i in range(4, 8) if i % 2 == 0]
                    else:
                        search_indices = [i for i in range(4, 8) if i % 2 == 1]
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
                        search_indices = [i + 8 for i in range(8)]
                    elif q_food == 'chicken':
                        search_indices = [i * 2 + 8 for i in range(4)]
                    else:
                        search_indices = [i * 2 + 1 + 8 for i in range(4)]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [i * 4 + 8 for i in range(2)] + [i * 4 + 1 + 8 for i in range(2)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 + 8 for i in range(2)]
                    else:
                        search_indices = [i * 4 + 1 + 8 for i in range(2)]
                else:
                    if q_food == '-':
                        search_indices = [i * 4 + 2 + 8 for i in range(2)] + [i * 4 + 3 + 8 for i in range(2)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 + 2 + 8 for i in range(2)]
                    else:
                        search_indices = [i * 4 + 3 + 8 for i in range(2)]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [i + 8 for i in range(4)]
                    elif q_food == 'chicken':
                        search_indices = [i + 8 for i in range(4) if i % 2 == 0]
                    else:
                        search_indices = [i + 8 for i in range(4) if i % 2 == 1]
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
                        search_indices = [i + 8 for i in range(4, 8)]
                    elif q_food == 'chicken':
                        search_indices = [i + 8 for i in range(4, 8) if i % 2 == 0]
                    else:
                        search_indices = [i + 8 for i in range(4, 8) if i % 2 == 1]
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
                        search_indices = [i + 16 for i in range(8)]
                    elif q_food == 'chicken':
                        search_indices = [i * 2 + 16 for i in range(4)]
                    else:
                        search_indices = [i * 2 + 1 + 16 for i in range(4)]
                elif q_career == 'junior':
                    if q_food == '-':
                        search_indices = [i * 4 + 16 for i in range(2)] + [i * 4 + 1 + 16 for i in range(2)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 + 16 for i in range(2)]
                    else:
                        search_indices = [i * 4 + 1 + 16 for i in range(2)]
                else:
                    if q_food == '-':
                        search_indices = [i * 4 + 2 + 16 for i in range(2)] + [i * 4 + 3 + 16 for i in range(2)]
                    elif q_food == 'chicken':
                        search_indices = [i * 4 + 2 + 16 for i in range(2)]
                    else:
                        search_indices = [i * 4 + 3 + 16 for i in range(2)]
            elif q_job == 'backend':
                if q_career == '-':
                    if q_food == '-':
                        search_indices = [i + 16 for i in range(4)]
                    elif q_food == 'chicken':
                        search_indices = [i + 16 for i in range(4) if i % 2 == 0]
                    else:
                        search_indices = [i + 16 for i in range(4) if i % 2 == 1]
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
                        search_indices = [i + 16 for i in range(4, 8)]
                    elif q_food == 'chicken':
                        search_indices = [i + 16 for i in range(4, 8) if i % 2 == 0]
                    else:
                        search_indices = [i + 16 for i in range(4, 8) if i % 2 == 1]
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
            for test in leaf[search_index]:
                if test >= q_test:
                    passed += 1
        answer[index] = passed
    
    return answer

print(solution(["java backend junior pizza 250", "cpp frontend junior pizza 250"], ["java and backend and junior and pizza 300", "- and - and junior and pizza 150"]))