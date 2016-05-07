import sys

import pygame

def capture(board, x, y, playerColor, other):
    score = 0
    case = [[-1,-1], [0,-1], [1,-1],
            [-1, 0], [0, 0], [1, 0],
            [-1, 1], [0, 1], [1, 1]]
    for i in case:
        if (y + 3 * i[0] < 19 and x + 3 * i[1] < 19):
            if (board[y + 1 * i[0]][x + 1 * i[1]] == other and board[y + 2 * i[0]][x + 2 * i[1]] == other and
                board[y + 3 * i[0]][x + 3 * i[1]] == playerColor):
                board[y + 1 * i[0]][x + 1 * i[1]] = None
                board[y + 2 * i[0]][x + 2 * i[1]] = None
                score += 2
    return (score, board)

def checkPatern3(l, player):
    #TODO Smooth
    return(True)

def getDouble3():
    nb3 = 0
    for i in [[0, 1], [1, 0], [1, 1], [-1, 1]]:
        if (checkPatern3([board[y - 1 * i[0]][x - 1 * i[1]], board[y + 1 * i[0]][x + 1 * i[1]], board[y + 2 * i[0]][x + 2 * i[1]], board[y + 3 * i[0]][x + 3 * i[1]], board[y + 4 * i[0]][x + 4 * i[1]]], player) or
            checkPatern3([board[y - 4 * i[0]][x - 4 * i[1]], board[y - 3 * i[0]][x - 3 * i[1]], board[y - 2 * i[0]][x - 2 * i[1]], board[y - 1 * i[0]][x - 1 * i[1]], board[y + 1 * i[0]][x + 1 * i[1]]], player) or
            checkPatern3([board[y - 2 * i[0]][x - 2 * i[1]], board[y - 1 * i[0]][x - 1 * i[1]], board[y + 1 * i[0]][x + 1 * i[1]], board[y + 2 * i[0]][x + 2 * i[1]], board[y + 3 * i[0]][x + 3 * i[1]]], player)):
            nb3 += 1
    return(nb3)

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
            if (cx >= 0 and cy >= 0 and cx < 19  and cy < 19):
                if (cBoard[cy][cx] ==  None):
                    cBoard[cy][cx] = player
                    if(True):
                        """↑ function_getDouble3 >= 2 ↑"""
                        print('checkDouble3 -> Nope')
                    else:
                        print('checkDouble3 -> Yeah')

def isBreakable(d, x, y, p, b):
    cx = x
    cy = y
    case = [[0,1], [1,1], [1,0], [1, -1]]
    e = 'w' if p == 'b' else 'b'
    print (d)
    if (((cy == 0 or cy == 18) and (d[0] == 0 and d[1] == -1)) or
        ((cx == 0 or cx == 18) and (d[0] == -1 and d[1] == 0))):
        print('x 0 ou 18')
        return (False)
    for i in range(0,5):
        cx = x + d[1] * i
        cy = y + d[0] * i
        for c in case:
            dx = cx - 2 * c[1]
            dy = cy - 2 * c[0]
            nb = 0
            for j in range(0,5):
                ccx = dx + j * c[1]
                ccy = dy + j * c[0]
                if not ((ccx > 18 or ccx < 0) or (ccy > 18 or ccy < 0)):
                    if b[ccy][ccx] == e and (nb == 0 or nb == 2):
                        nb += 3
                    elif b[ccy][ccx] == e and nb != 1:
                        nb = 0
                    elif b[ccy][ccx] == p and (nb <= 1 or nb >= 3):
                        nb += 1
                    elif b[ccy][ccx] == p and nb == 2:
                        nb = 0
                    elif b[ccy][ccx] == None:
                        nb = 0
                if nb == 5:
                    return (True)
    return (False)

def check5(board, x, y, color):
    case = [[0,1], [1,1], [1,0], [1, -1]]
    for c in case:
        dx = x - 4 * c[1]
        dy = y - 4 * c[0]
        nb = 0
        for i in range(0,9):
            cx = dx + i * c[1]
            cy = dy + i * c[0]
            if not ((cx > 18 or cx < 0) or (cy > 18 or cy < 0)):
                if board[cy][cx] == color:
                    nb += 1
                    if nb == 5:
                        if not (isBreakable([-c[0], -c[1]], cx, cy, color, board)):
                            return (color)
                else:
                    nb = 0
    return (0)
