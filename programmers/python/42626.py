import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] < K:
            m = heapq.heappop(scoville)
            n = heapq.heappop(scoville)
            heapq.heappush(scoville, m + 2 * n)
            answer += 1
        else:
            break
    if scoville[0] < K:
        answer = -1
        
    return answer

print(solution([1, 2, 3], 11))