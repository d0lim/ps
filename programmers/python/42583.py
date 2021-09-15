from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    deq = deque(truck_weights)

    on_bridge = []
    while True:
        if len(deq) > 0:
            truck = deq.popleft()
        else:
            truck = None
        # 일단 다리 위 트럭을 한칸씩 땡겨주자
        if len(on_bridge) > 0:
            for i, t in enumerate(on_bridge):
                t[1] += 1
            for i, t in enumerate(on_bridge):
                if t[1] > bridge_length:
                    on_bridge.remove(t)
        # 그리고 트럭을 한번 올려보자
        if truck != None and sum(e for e, t in on_bridge) + truck <= weight:
            on_bridge.append([truck, 1])
        elif truck != None:
            deq.appendleft(truck)
        answer += 1
        if len(deq) == 0 and len(on_bridge) == 0:
            break

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
