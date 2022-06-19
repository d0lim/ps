N = int(input())
M = int(input())
S = input()

count = 0
pattern = 0
i = 1
while i < M - 1:
    if S[i - 1] == "I" and S[i] == "O" and S[i + 1] == "I":
        pattern += 1
        if pattern == N:
            # 또 만족할 수 있음
            pattern -= 1
            count += 1
        # 2번 뛰기
        i += 1
    else:
        pattern = 0
    i += 1

print(count)
