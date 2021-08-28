from collections import deque


def calc(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        print("?????????")
        return 0


def calculate(op_list, equation):
    deq = deque()
    for i in range(1, len(equation), 2):
        if op_list[i // 2] == 1:
            deq.append(calc(int(equation[i - 1]), equation[i], int(equation[i + 1])))
        else:
            # 만약 앞의 연산자가 괄호였다면
            if i >= 3 and op_list[i // 2 - 1] == 1:
                deq.append(equation[i])
                if len(op_list) - 1 == i // 2:
                    deq.append(int(equation[i + 1]))
            else:
                deq.append(int(equation[i - 1]))
                deq.append(equation[i])
                if len(op_list) - 1 == i // 2:
                    deq.append(int(equation[i + 1]))
    result = deq.popleft()
    while len(deq) > 0:
        op = deq.popleft()
        b = deq.popleft()
        result = calc(result, op, b)
    return result


n = int(input())
e = input()
if n == 1:
    print(e)
else:
    op_len = n // 2

    op_available = {
        0: [(0, 0, 0, 0, 0, 0, 0, 0, 0)],
        1: [(0, 0, 0, 0, 0, 0, 0, 0, 1)],
        2: [(0, 0, 0, 0, 0, 0, 0, 1, 0)],
    }

    for i in range(2, op_len):
        op_pow = 2 ** i
        # 일단 0에 대한 항 먼저 추가해줌
        tmp = (0,) * (9 - i - 1) + (1,) + (0,) * i
        op_available[op_pow] = [tmp]
        # 이제 반복문 돌면서, 1 2 4 8... 에 대한 것들 추가
        j = 1
        while j < op_pow / 2:
            tmp = (0,) * (9 - i - 1) + (1,)
            for k in op_available[j]:
                tmp += k[9 - i :]
                op_available[op_pow].append(tmp)
                tmp = (0,) * (9 - i - 1) + (1,)
            j <<= 1
    op_list = op_available[0]
    for i in range(op_len):
        op_list += op_available[2 ** i]

    op_list = [sub[9 - op_len :] for sub in op_list]

    m = -999999999999999
    for opl in op_list:
        v = calculate(opl, e)
        m = v if v > m else m

    print(m)