# -*- coding: utf-8 -*-
# @author: beauge_z

"""
This module contain the basic gameplay functions.
"""
import pygame

import ai
from referee import Referee


def init_board():
    """
    Create the board.
    """
    board = list()
    for cpt_y in range(0, 19):
        to_append = list()
        cpt_y = cpt_y
        for cpt_x in range(0, 19):
            to_append.append(None)
            cpt_x = cpt_x
        board.append(to_append)
    return board


def r_false(coord_x=0, coord_y=0):
    """
    return False.
    Needed to attribute function for options.
    """
    _ = coord_x, coord_y
    return False


def r_true(coord_x=0, coord_y=0):
    """
    return False.
    Needed to attribute function for options.
    """
    _ = coord_x, coord_y
    return True


def update_stone_player(screen, player_color):
    """
    Move the stone along the mouse cursor.
    """
    coord_x, coord_y = pygame.mouse.get_pos()
    white = pygame.image.load('./img/stoneW.png').convert_alpha()
    black = pygame.image.load('./img/stoneB.png').convert_alpha()
    coord_x = int((coord_x - 5) / 40) * 40 + 5
    coord_y = int((coord_y - 5) / 40) * 40 + 5
    screen.blit(white if player_color == 'w' else black, (round(coord_x), round(coord_y)))


def display_board(screen, board):
    """
    Display the board and stones.
    """
    background = pygame.image.load('./img/Goban.jpg')
    white = pygame.image.load('./img/stoneW.png').convert_alpha()
    black = pygame.image.load('./img/stoneB.png').convert_alpha()
    screen.blit(background, (0, 0))
    for cpt_y in range(0, 19):
        for cpt_x in range(0, 19):
            coord_y = cpt_y * 40 + 5
            coord_x = cpt_x * 40 + 5
            if board[cpt_y][cpt_x] == 'b':
                screen.blit(black, (round(coord_x), round(coord_y)))
            elif board[cpt_y][cpt_x] == 'w':
                screen.blit(white, (round(coord_x), round(coord_y)))


def load_p_vs_ai(screen):
    """
    Load the gamemode against an AI.
    """
    run = True
    board = init_board()
    player_color = 'b'  # set_color_player
    ref = Referee()
    ai_turn = True if player_color == 'w' else False
    while run:
        display_board(screen, board)
        if ai_turn:
            pos = ai.ai_play(board, ('b' if player_color == 'w' else 'w'))
            rboard, score, msg = ref.set_stone(board, ('b' if player_color == 'w' else 'w'), pos)
            if rboard is not None:
                board = rboard
                win = ref.check5(board, pos, ('b' if player_color == 'w' else 'w'))
                ai_turn = False
            run = ref.display_score(score, ('b' if player_color == 'w' else 'w'), win, msg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not ai_turn:
                coord_x, coord_y = pygame.mouse.get_pos()
                coord_x = int((coord_x - 5) / 40)
                coord_y = int((coord_y - 5) / 40)
                rboard, score, msg = ref.set_stone(board, player_color, [coord_y, coord_x])
                if rboard is not None:
                    board = rboard
                    win = ref.check5(board, [coord_y, coord_x], player_color)
                    ai_turn = True
                run = ref.display_score(score, player_color, win, msg)
        update_stone_player(screen, player_color)
        pygame.display.update()
    return True


def load_p_vs_p(screen):
    """
    Load the gamemode PvP.
    """
    run = True
    board = init_board()
    player_color = 'b'
    ref = Referee()
    while run:
        display_board(screen, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coord_x, coord_y = pygame.mouse.get_pos()
                coord_x = int((coord_x - 5) / 40)
                coord_y = int((coord_y - 5) / 40)
                rboard, score, msg = ref.set_stone(board, player_color, [coord_y, coord_x])
                if rboard is not None:
                    board = rboard
                    win = ref.check5(board, [coord_y, coord_x], player_color)
                    player_color = 'b' if player_color == 'w' else 'w'
                run = ref.display_score(score, player_color, win, msg)
        update_stone_player(screen, player_color)
        pygame.display.update()
    return True
