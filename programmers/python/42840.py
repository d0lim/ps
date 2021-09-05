def solution(answers):
    # 1: 1 2 3 4 5
    # 2: 2 1 2 3 2 3 2 5
    # 3: 3 3 1 1 2 2 4 4 5 5
    supo = {
        "1": [1, 2, 3, 4, 5],
        "2": [2, 1, 2, 3, 2, 4, 2, 5],
        "3": [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    scores = {}
    for key, pattern in supo.items():
        length = len(pattern)
        i = 0
        correct = 0
        for ans in answers:
            if pattern[i] == ans:
                correct += 1
            i = (i + 1) % length
        scores[key] = correct
    
    m = 0
    answer = []
    for key, score in scores.items():
        if score > m:
            m = score
            answer = [int(key)]
        elif score == m:
            answer.append(int(key))
        
    return answer

def solution_good(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result