import sys

import pygame

def capture(board, x, y, playerColor, other):
    score = 0
    case = [[-1,-1], [0,-1], [1,-1],
            [-1, 0], [0, 0], [1, 0],
            [-1, 1], [0, 1], [1, 1]]
    for i in case:
        if board[y + 1 * i[0]][x + 1 * i[1]] == other and board[y + 2 * i[0]][x + 2 * i[1]] == other and board[y + 3 * i[0]][x + 3 * i[1]] == playerColor:
            board[y + 1 * i[0]][x + 1 * i[1]] = None
            board[y + 2 * i[0]][x + 2 * i[1]] = None
            score += 2
    return (score, board)

def checkDouble3(board, x, y, player):
    cBoard = list()
    for j in board:
        a = list()
        for i in j:
            a.append(i)
        cBoard.append(a)
    for i in range(0, 8):
        for j in range(0, 8):
            cx = x - 4 + j
            cy = y - 4 + i
            if (cx >= 0 && cy >= 0 && cx < 19  && cy < 19):
                if (cBoard[cy][cx] ==  None):
                    cBoard[cy][cx] = player
                    if(True):
                        """↑ function_getDouble3 >= 2 ↑"""
                        print('checkDouble3 -> Nope')
                    else:
                        print('checkDouble3 -> Yeah')

def check5(board, x, y, color):
        case = [[-1,-1], [0,-1], [1,-1],
                [-1, 0], [0, 0], [1, 0],
                [-1, 1], [0, 1], [1, 1]]
        nb1 = 1
        nb2 = 1
        m = (len(case))
        for i in range(0, int(len(case)/2)):
            while board[y + case[i][1] * nb1][x + case[i][0] * nb1] == color:
                nb1 += 1
                if nb1 == 5:
                    return(color)
            while board[y + case[m - i - 1][1] * nb2][x + case[m - i - 1][0] * nb2] == color:
                nb2 += 1
                if nb2 == 5 or nb2+nb1-2 == 5:
                    return(color)
            if nb1+nb2-2 == 5:
                return(color)
        return(0)
