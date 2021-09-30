import sys


def compute_lps(pat, lps):
    l = 0
    i = 1
    # lps[0] == 0
    while i < len(pat):
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(pat, txt):
    m = len(pat)
    n = len(txt)

    lps = [0] * m

    lps = compute_lps(pat, lps)

    i = 0
    j = 0
    cnt = 0
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == m:
            cnt += 1
            j = lps[j - 1]

    return cnt


N = int(sys.stdin.readline().rstrip())
_ = sys.stdin.readline()
S = sys.stdin.readline().rstrip()

P = "IO" * N + "I"

print(kmp_search(P, S))
