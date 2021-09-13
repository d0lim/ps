def solution(name):
    answer = 0

    m = len(name) - 1
    for i, c in enumerate(name):
        answer += (
            ord(c) - ord("A") if ord(c) - ord("A") <= 13 else 26 - ord(c) + ord("A")
        )

        n = i + 1
        while n < len(name) and name[n] == "A":
            n += 1
        m = min(m, 2 * i + len(name) - n)
    answer += m
    return answer


# print(solution("JAN"))
print(solution("ZZAAAZZ"))
