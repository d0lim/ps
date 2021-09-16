from collections import deque


def solution(prices):
    answer = []
    deq = deque(prices)
    while len(deq) > 0:
        ans = 0
        tmp_deq = deque()
        top = deq.popleft()
        while len(deq) > 0:
            n = deq.popleft()
            tmp_deq.appendleft(n)
            ans += 1
            if n < top:
                answer.append(ans)
                deq.extendleft(tmp_deq)
                break
        else:
            answer.append(ans)
            deq.extendleft(tmp_deq)

    return answer


print(solution([1, 2, 3, 2, 3]))
