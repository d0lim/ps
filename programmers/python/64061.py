from collections import deque


def pick(board, move):
    for row in board:
        if row[move - 1] != 0:
            picked = row[move - 1]
            row[move - 1] = 0
            return board, picked
    else:
        return board, 0


def solution(board, moves):
    answer = 0
    bascket = deque()
    for move in moves:
        board, picked = pick(board, move)
        if picked != 0:
            if len(bascket) != 0:
                top = bascket.popleft()
                if top == picked:
                    answer += 2
                    continue
                else:
                    bascket.appendleft(top)
            bascket.appendleft(picked)

    return answer
