import math

def solution(numbers, target):
    length = 2 ** (len(numbers) + 1)
    graph = [0] * length

    for i in range(2, length):
        parent = i // 2
        # 짝
        if i % 2 == 0:
            graph[i] = graph[parent] + numbers[int(math.log(i, 2)) - 1]
        # 홀
        else:
            graph[i] = graph[parent] - numbers[int(math.log(i, 2)) - 1]
    
    result = graph[length // 2:]
    
    return result.count(target)

print(solution([1, 1, 1, 1, 1], 3))