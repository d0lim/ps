

def solution(info, query):
    answer = [0] * len(query)

    dic = {"java": set(), "cpp": set(), "python": set(), "backend": set(), "frontend": set(), "junior": set(), "senior": set(), "chicken": set(), "pizza": set()}
    for index, i in enumerate(info):
        splitted_info = i.split()
        dic[splitted_info[0]].add(index)
        dic[splitted_info[1]].add(index)
        dic[splitted_info[2]].add(index)
        dic[splitted_info[3]].add(index)
    for index, q in enumerate(query):
        splitted_query = q.split(' and ')
        splitted_query = splitted_query[:-1] + splitted_query[-1].split()
        q_test = int(splitted_query[4])

        search_set = set([i for i in range(len(info))])
        for i in range(4):
            if splitted_query[i] != '-':
                search_set = search_set & dic[splitted_query[i]]

        for s in search_set:
            if int(info[s].split()[4]) >= q_test:
                answer[index] += 1

    return answer
        


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))