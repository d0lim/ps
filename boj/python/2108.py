from functools import reduce
import sys

N = int(sys.stdin.readline().rstrip())
l = []
for _ in range(N):
    l.append(int(sys.stdin.readline().rstrip()))

l = list(sorted(l))

length = len(l)

mean = int(round(reduce(lambda x, y: x + y, l) / length))
mid = 0
if length % 2 == 0:
    mid = round((l[length // 2 - 1] + l[length // 2]) / 2)
else:
    mid = l[length // 2]

mode_list = []
will_mode = [0, 0]
temp_mode = [0, 0]
for i in range(length):
    if i == 0:
        temp_mode = [l[i], 1]
        if length == 1:
            mode_list.append(l[i])
    elif i > 0 and temp_mode[0] == l[i]:
        temp_mode[1] += 1
        if i == length - 1:
            if will_mode[1] < temp_mode[1]:
                mode_list = [temp_mode[0]]
                will_mode[0] = temp_mode[0]
                will_mode[1] = temp_mode[1]
            elif will_mode[1] == temp_mode[1]:
                mode_list.append(temp_mode[0])
    else:
        if will_mode[1] < temp_mode[1]:
            mode_list = [temp_mode[0]]
            will_mode[0] = temp_mode[0]
            will_mode[1] = temp_mode[1]
        elif will_mode[1] == temp_mode[1]:
            mode_list.append(temp_mode[0])
        temp_mode = [l[i], 1]


mode = 0
if len(mode_list) > 1:
    mode_list = list(sorted(mode_list))
    mode = mode_list[1]
else:
    mode = mode_list[0]
    

rg = l[-1] - l[0]

print(mean)
print(mid)
print(mode)
print(rg)