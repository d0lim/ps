def solution(n, lost, reserve):
    training = [1] * n
    for i in reserve:
        training[i - 1] = 2
    for i in lost:
        training[i - 1] -= 1
    for i, s in enumerate(training):
        if s == 0:
            if i == 0:
                if training[i + 1] == 2:
                    training[i] += 1
                    training[i + 1] -= 1
            elif i == len(training) - 1:
                if training[i - 1] == 2:
                    training[i] += 1
                    training[i - 1] -= 1
            else:
                if training[i - 1] == 2:
                    training[i] += 1
                    training[i - 1] -= 1
                elif training[i + 1] == 2:
                    training[i] += 1
                    training[i + 1] -= 1

    return sum(i > 0 for i in training)
