from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    day = deque()
    for i in range(len(progresses)):
        day.append(ceil((100 - progresses[i]) / speeds[i]))
    while len(day) > 0:
        num = 1
        top = day.popleft()
        while len(day) > 0:
            waiting = day.popleft()
            if waiting <= top:
                num += 1
            else:
                day.appendleft(waiting)
                break
        answer.append(num)
    return answer

print(solution([93, 30, 55], [1, 30, 5]	))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))