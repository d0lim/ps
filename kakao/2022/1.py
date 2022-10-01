def convert(n, k):
    max_pow = 0
    pows = []
    while True:
        if pow(k, max_pow) > n:
            break
        pows.append(pow(k, max_pow))
        max_pow += 1
    res = []
    for p in reversed(pows):
        d = n // p
        res.append(d)
        n = n % p
    return "".join(map(str, res))


def prime_check(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def cnt_primes(s):
    nums = list(map(int, filter(lambda x: x != "", s.split("0"))))
    if not nums:
        return 0
    return len(list(filter(prime_check, nums)))


def solution(n, k):
    return cnt_primes(convert(n, k))


print(solution(10, 10))
