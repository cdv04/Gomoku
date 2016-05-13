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
    # TODO return move


def ai_check_win(board, coord, color, depth):
    """
    Check if the move made the AI win.
    """
    coord_x = coord[0]
    coord_y = coord[1]
    ref = Referee()
    if ref.check5(board, [int((coord_y - 5) / 40), int((coord_x - 5) / 40)], color):
        board[coord_y][coord_x] = None
        if not depth:
            return [coord_x, coord_y]
        return float('Inf')
    return None
