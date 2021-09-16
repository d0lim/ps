def solution(citations):
    citations = sorted(citations)
    for i, c in enumerate(citations):
        if c >= len(citations) - i:
            return len(citations) - i
    else:
        return 0
