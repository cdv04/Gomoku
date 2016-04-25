import sys

import pygame

def capture(board, x, y, playerColor, other):
    score = 0
    for i in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        if board[y + 1 * i[0]][x + 1 * i[1]] == other and board[y + 2 * i[0]][x + 2 * i[1]] == other and board[y + 3 * i[0]][x + 3 * i[1]] == playerColor:
            board[y + 1 * i[0]][x + 1 * i[1]] = None
            board[y + 2 * i[0]][x + 2 * i[1]] = None
            score += 2
    return (score, board)

def check5(board, x, y, color):
    alignH = 1
    alignV = 1
    alignD1 = 1
    alignD2 = 1
    xt = x - 1
    yt = y
    while (xt >= 0 and board[yt][xt] == color):
        xt -= 1
        alignH += 1
    xt = x + 1
    yt = y
    while (xt < 19 and board[yt][xt] == color):
        xt += 1
        alignH += 1
    xt = x
    yt = y - 1
    while (yt >= 0 and board[yt][xt] == color):
        yt -= 1
        alignV += 1
    xt = x
    yt = y + 1
    while (yt < 19 and board[yt][xt] == color):
        yt += 1
        alignV += 1
    xt = x - 1
    yt = y - 1
    while (xt >= 0 and yt >= 0 and board[yt][xt] == color):
        xt -= 1
        yt -= 1
        alignD1 += 1
    xt = x + 1
    yt = y + 1
    while (xt < 19 and yt < 19 and board[yt][xt] == color):
        xt += 1
        yt += 1
        alignD1 += 1
    xt = x - 1
    yt = y + 1
    while (xt >= 0 and yt < 19 and board[yt][xt] == color):
        xt -= 1
        yt += 1
        alignD2 += 1
    xt = x + 1
    yt = y - 1
    while (xt < 19 and yt >= 0 and board[yt][xt] == color):
        xt += 1
        yt -= 1
        alignD2 += 1
    if(max(alignH,alignV,alignD1,alignD2) == 5):
        return color
    else:
        return 0
