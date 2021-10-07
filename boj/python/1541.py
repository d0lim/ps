import sys
import re


def is_zero(s):
    if len(s) == s.count("0"):
        return True
    return False


formula = sys.stdin.readline().rstrip()

operators = ["+"] + [x for x in formula if x == "+" or x == "-"]

splitted = re.split(r"[+-]", formula)
splitted = list(map(int, map(lambda s: "0" if is_zero(s) else s.lstrip("0"), splitted)))
zipped = list(zip(operators, splitted))

res = 0
flag = False
for z in zipped:
    if flag:
        if z[0] == "+":
            res -= z[1]
        else:
            res -= z[1]
    else:
        if z[0] == "+":
            res += z[1]
        else:
            flag = True
            res -= z[1]

print(res)
