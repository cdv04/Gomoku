# -*- coding: utf-8 -*-
# @author: beauge_z

"""
This module is the AI of the Gomoku game.
"""

from referee import Referee


def ai_play(board, color):
    """
    Return the move done by the AI.
    """
    copied_board = list()
    for j in board:
        to_append = list()
        for i in j:
            to_append.append(i)
        copied_board.append(to_append)
    return ai_alpha_beta(copied_board, color, 0, float('-Inf'), float('Inf'))


def ai_check_win(board, coord, color, depth):
    """
    Check if the move made the AI win.
    """
    coord_x = coord[0]
    coord_y = coord[1]
    ref = Referee()
    if ref.check5(board, coord, color):
        board[coord_y][coord_x] = None
        if not depth:
            return True
        return False
    return False


def ai_alpha_beta(board, color, depth, alpha, beta):
    """
    Algo min-max with calibration alpha-beta
    """
    if depth == 4:
        return ai_estimate(board) if color == 'b' else -ai_estimate(board)
    best = float('-Inf')
    estim = 0
    play = None
    enemy = 'b' if color == 'w' else 'b'
    for coord_x in range(0, 19):
        for coord_y in range(0, 19):
            if not play:
                play = [coord_y, coord_x]
            board[coord_y][coord_x] = color
            if ai_check_win(board, [coord_y, coord_x], color, depth):
                return [coord_y, coord_x]
            estim = -ai_alpha_beta(board, enemy, depth + 1, -beta, -alpha)
            if estim > best:
                best = estim
                if best > alpha:
                    alpha = best
                    play = [coord_y, coord_x]
                    if alpha >= beta:
                        board[coord_y][coord_x] = None
                        return play if not depth else best
                board[coord_y][coord_x] = None
        if not depth:
            return play
        elif play:
            return best
        return 0


def ai_estimate(board):
    """
    Return an estimation of the position.
    """
    estimation = 0
    for coord_x in range(0, 19):
        for coord_y in range(0, 19):
            if board[coord_y][coord_x] == 'b':
                estimation += ai_analyse(board, coord_x, coord_y)
            elif board[coord_y][coord_x] == 'w':
                estimation -= ai_analyse(board, coord_x, coord_y)
    return estimation


def ia_diagonal2_analyse(board, coord_x, coord_y, color):
    """
    Analyse the board (diagonal ymax->ymin;xmin->xmax)
    Called by ai_analyse
    """
    cpt = 0
    bonus = 0
    i = coord_x
    j = coord_y
    while i >= 0 and j < 19:
        if board[j][i] is None:
            cpt += 1
        elif board[j][i] == color:
            cpt += 1
            bonus += 1
        else:
            break
        i -= 1
        j += 1
    cpt += 1
    center = cpt
    i = coord_x
    j = coord_y
    while i < 19 and j >= 0:
        if board[j][i] is None:
            cpt += 1
        elif board[j][i] == color:
            cpt += 1
            bonus += 1
        else:
            break
        i += 1
        j -= 1
    if cpt >= 5:
        return cpt * 1 + bonus * 1 + (1 - abs(center / (cpt - 1) - 0.5)) * cpt * 2
    return 0


def ia_diagonal1_analyse(board, coord_x, coord_y, color):
    """
    Analyse the board (diagonal ymin->ymax;xmin->xmax)
    Called by ai_analyse
    """
    cpt = 0
    bonus = 0
    i = coord_x
    j = coord_y
    while i >= 0 and j >= 0:
        if board[j][i] is None:
            cpt += 1
        elif board[j][i] == color:
            cpt += 1
            bonus += 1
        else:
            break
        i -= 1
        j -= 1
    cpt += 1
    center = cpt
    i = coord_x
    j = coord_y
    while i < 19 and j < 19:
        if board[j][i] is None:
            cpt += 1
        elif board[j][i] == color:
            cpt += 1
            bonus += 1
        else:
            break
        i += 1
        j += 1
    if cpt >= 5:
        return cpt * 1 + bonus * 1 + (1 - abs(center / (cpt - 1) - 0.5)) * cpt * 2
    return 0


def ia_horizontal_analyse(board, coord_x, coord_y, color):
    """
    Analyse the board (horizontal)
    Called by ai_analyse
    """
    cpt = 0
    bonus = 0
    chck = False
    for i in range(0, 19):
        if i == coord_x:
            cpt += 1
            center = cpt
            chck = True
        if board[coord_y][i] is None:
            cpt += 1
        elif board[coord_y][i] == color:
            cpt += 1
            bonus += 1
        else:
            if chck:
                i = 19
            else:
                cpt = 0
                bonus = 0
    if cpt >= 5:
        return cpt * 1 + bonus * 1 + (1 - abs(center / (cpt - 1) - 0.5)) * cpt * 2
    return 0


def ia_vertical_analyse(board, coord_x, coord_y, color):
    """
    Analyse the board (vertical)
    Called by ai_analyse
    """
    cpt = 0
    bonus = 0
    chck = False
    for j in range(0, 19):
        if j == coord_y:
            cpt += 1
            center = cpt
            chck = True
        if board[j][coord_x] is None:
            cpt += 1
        elif board[j][coord_x] == color:
            cpt += 1
            bonus += 1
        else:
            if chck:
                j = 19
            else:
                cpt = 0
                bonus = 0
    if cpt >= 5:
        return cpt * 1 + bonus * 1 + (1 - abs(center / (cpt - 1) - 0.5)) * cpt * 2
    return 0


def ai_analyse(board, coord_x, coord_y):
    """
    Calcul the possibility
    """
    color = board[coord_y][coord_x]
    estimation = 0
    estimation += ia_vertical_analyse(board, coord_x, coord_y, color)
    estimation += ia_horizontal_analyse(board, coord_x, coord_y, color)
    estimation += ia_diagonal1_analyse(board, coord_x, coord_y, color)
    estimation += ia_diagonal2_analyse(board, coord_x, coord_y, color)
    return estimation
