s = input()

l = len(s)

rs = []

for i in range(1, l - 1):
    for j in range(i + 1, l):
        first = s[:i]
        second = s[i:j]
        third = s[j:]
        rs.append(
            "".join(reversed(first))
            + "".join(reversed(second))
            + "".join(reversed(third))
        )

print(sorted(rs)[0])
