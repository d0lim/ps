import math

answer = 0


def dfs(numbers, i, acc, target):
    global answer
    if i == len(numbers):
        if acc == target:
            answer += 1
        return

    dfs(numbers, i + 1, acc + numbers[i], target)
    dfs(numbers, i + 1, acc - numbers[i], target)


def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
