from collections import deque

case_num = int(input())

for i in range(case_num):
    # input
    doc, index = input().split()
    doc = int(doc)
    index = int(index)
    queue = deque(map(int, input().split()))

    # logic
    n = 0
    while len(queue) > 0:
        length = len(queue)

        top = queue.popleft()
        if index == 0:
            if len(queue) == 0:
                n += 1
                break

            if max(queue) > top:
                queue.append(top)
                index = length - 1
            else:
                n += 1
                break
        else:
            if len(queue) == 0:
                print("It must not be happened!")

            if max(queue) > top:
                queue.append(top)
            else:
                n += 1

            index -= 1

    print(n)
