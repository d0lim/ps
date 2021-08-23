def failure_function(s):
    ff = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = ff[j - 1]

        if s[i] == s[j]:
            j += 1
            ff[i] = j
    return ff


def kmp(s, p):
    ff = failure_function(p)
    n = len(s)
    m = len(p)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = ff[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                print(1)
                return
            else:
                j += 1

    else:
        print(0)


S = input()
P = input()


kmp(S, P)