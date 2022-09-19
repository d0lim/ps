s = input()

l = len(s)


for i in range(l):
    check = s
    sub = check[:i]
    check += "".join(reversed(sub))
    cl = len(check)
    mid = cl // 2
    odd = (i + l) % 2 == 1

    if odd:
        if check[:mid] == "".join(reversed(check[mid + 1 :])):
            print(l + i)
            break
    else:
        if check[:mid] == "".join(reversed(check[mid:])):
            print(l + i)
            break
