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

def checkPatern3(l, player):
    #TODO Smooth
    return(True)

def checkFree3():
    nb3 = 0
    if (checkPatern3([board[y][x - 1], board[y][x + 1], board[y][x + 2], board[y][x + 3], board[y][x + 4]], player) or
        checkPatern3([board[y][x - 4], board[y][x - 3], board[y][x - 2], board[y][x - 1], board[y][x + 1]], player) or
        checkPatern3([board[y][x - 2], board[y][x - 1], board[y][x + 1], board[y][x + 2], board[y][x + 3]], player)):
        nb3 += 1
    if (checkPatern3([board[y - 1][x], board[y + 1][x], board[y + 2][x], board[y + 3][x], board[y + 4][x]], player) or
        checkPatern3([board[y - 4][x], board[y - 3][x], board[y - 2][x], board[y - 1][x], board[y + 1][x]], player) or
        checkPatern3([board[y - 2][x], board[y - 1][x], board[y + 1][x], board[y + 2][x], board[y + 3][x]], player)):
        nb3 += 1
    if (checkPatern3([board[y - 1][x - 1], board[y + 1][x + 1], board[y + 2][x + 2], board[y + 3][x + 3], board[y + 4][x + 4]], player) or
        checkPatern3([board[y - 4][x - 4], board[y - 3][x - 3], board[y - 2][x - 2], board[y - 1][x - 1], board[y + 1][x + 1]], player) or
        checkPatern3([board[y - 2][x - 2], board[y - 1][x - 1], board[y + 1][x + 1], board[y + 2][x + 2], board[y + 3][x + 3]], player)):
        nb3 += 1
    if (checkPatern3([board[y + 4][x - 4], board[y + 3][x - 3], board[y + 2][x - 2], board[y + 1][x - 1], board[y - 1][x + 1]], player) or
        checkPatern3([board[y + 1][x - 1], board[y - 1][x + 1], board[y - 2][x + 2], board[y - 3][x + 3], board[y - 4][x + 4]], player) or
        checkPatern3([board[y + 2][x - 2], board[y + 1][x - 1], board[y - 1][x + 1], board[y - 2][x + 2], board[y - 3][x + 3]], player)):
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

def isBreakable(dir, x, y, p, b):
    cx = x
    cy = y
    e = 'w' if p == 'b' else 'b'
    for i in range(0,5):
        if (dir != 'L'):
            if ((b[cy][cx + 1] == p and (b[cy][cx + 2] == None or b[cy][cx + 2] != None) and b[cy][cx - 1] == e) or
                (b[cy][cx + 1] == p and b[cy][cx + 2] == e and (b[cy][cx - 1] == None or b[cy][cx - 1] != None)) or
                (b[cy][cx + 1] == e and b[cy][cx - 1] == p and (b[cy][cx - 2] == None or b[cy][cx - 2] != None)) or
                ((b[cy][cx + 1] == None or b[cy][cx + 1] != None) and b[cy][cx - 1] == p and b[cy][cx - 2] == e)):
                return (true)
        if (dir != 'C'):
            if ((b[cy + 1][cx] == p and (b[cy + 2][cx] == None or b[cy + 2][cx] != None) and b[cy - 1][cx] == e) or
                (b[cy + 1][cx] == p and b[cy + 2][cx] == e and (b[cy - 1][cx] == None or b[cy - 1][cx] != None)) or
                (b[cy + 1][cx] == e and b[cy - 1][cx] == p and (b[cy - 2][cx] == None or b[cy - 2][cx] != None)) or
                ((b[cy + 1][cx] == None or b[cy + 1][cx] != None) and b[cy - 1][cx] == p and b[cy - 2][cx] == e)):
                return (true)
        if (dir != 'D1'):
            if ((b[cy + 1][cx + 1] == p and (b[cy + 2][cx + 2] == None or b[cy + 2][cx + 2] != None) and b[cy - 1][cx - 1] == e) or
                (b[cy + 1][cx + 1] == p and b[cy + 2][cx + 2] == e and (b[cy - 1][cx - 1] == None or b[cy - 1][cx - 1] != None)) or
                (b[cy + 1][cx + 1] == e and b[cy - 1][cx - 1] == p and (b[cy - 2][cx - 2] == None or b[cy - 2][cx - 2] != None)) or
                ((b[cy + 1][cx + 1] == None or b[cy + 1][cx + 1] != None) and b[cy - 1][cx - 1] == p and b[cy - 2][cx - 2] == e)):
                return (true)
        if (dir != 'D2'):
            if ((b[cy + 1][cx - 1] == p and (b[cy + 2][cx - 2] == None or b[cy + 2][cx - 2] != None) and b[cy - 1][cx + 1] == e) or
                (b[cy + 1][cx - 1] == p and b[cy + 2][cx - 2] == e and (b[cy - 1][cx + 1] == None or b[cy - 1][cx + 1] != None)) or
                (b[cy + 1][cx - 1] == e and b[cy - 1][cx + 1] == p and (b[cy - 2][cx + 2] == None or b[cy + 2][cx + 2] != None)) or
                ((b[cy + 1][cx - 1] == None or b[cy + 1][cx - 1] != None) and b[cy - 1][cx + 1] == p and b[cy - 2][cx + 2] == e)):
                return (true)
        if dir == 'L':
            cx += 1
        elif dir == 'C':
            cy += 1
        elif dir == 'D1':
            cx += 1
            cy += 1
        elif dir == 'D2':
            cx -= 1
            cy -= 1
        else:
            print("[ERROR]: Unkown \'dir\'.", file=sys.stderr)
    return (false)

def check5(board, x, y, color):
        case = [[-1,-1], [0,-1], [1,-1],
                [-1, 0], [0, 0], [1, 0],
                [-1, 1], [0, 1], [1, 1]]
        caseL = ['D1', 'C', 'D2',
                'L', None, 'L',
                'D2', 'C', 'D1']
        nb1 = 1
        nb2 = 1
        m = (len(case))
        for i in range(0, int(len(case)/2)):
            while board[y + case[i][1] * nb1][x + case[i][0] * nb1] == color:
                nb1 += 1
                if nb1 == 5:
                    if (isBreakable(caseL[i])):
                        return(color)
            while board[y + case[m - i - 1][1] * nb2][x + case[m - i - 1][0] * nb2] == color:
                nb2 += 1
                if nb2 == 5 or nb2+nb1-2 == 5:
                    if (isBreakable(caseL[m - i - 1])):
                        return(color)
            if nb1+nb2-2 == 5:
                if (isBreakable(caseL[i])):
                    return(color)
        return(0)
