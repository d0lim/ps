def solution(clothes):
    answer = 1
    dic = {}
    
    for cloth in clothes:
        dic.setdefault(cloth[1], list())
        dic[cloth[1]].append(cloth[0])
    
    for v in dic.values():
        answer *= (len(v) + 1)
    print(dic)
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))