from itertools import permutations

def solution(numbers):
    answer = 0
    s = set()
    l = list(numbers)
    for i in range(1, len(l) + 1):
        p = list(permutations(l, i))
        for t in p:
            n_str = ''.join(t).lstrip('0')
            if n_str == '':
                continue
            s.add(int(n_str))

    sieve = [False, False] + [True] * (max(s) - 1)
    prime = []
    for i in range(2, max(s) + 1):
        if sieve[i]:
            prime.append(i)
            for j in range(i * 2, max(s) + 1, i):
                sieve[j] = False

    for e in s:
        if e in prime:
            answer += 1
    
    return answer

print(solution("17"))
print(solution("011"))