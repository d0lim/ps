from collections import deque, defaultdict


def solution(info, edges):
    adj = defaultdict(list)

    for s, e in edges:
        adj[s].append(e)

    visited = [False] * len(info)
    q = deque()

    answer = 0
    return answer
