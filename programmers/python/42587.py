from collections import deque


def solution(priorities, location):
    answer = 0
    loc = [1 if i == location else 0 for i in range(len(priorities))]
    deq = deque(zip(priorities, loc))
    while len(deq) > 1:
        p = deq.popleft()

        if p[0] >= max(deq, key=lambda e: e[0])[0]:
            answer += 1
            if p[1] == 1:
                return answer
        else:
            deq.append(p)

    return answer + 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([3], 0))
