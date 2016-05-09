# -*- coding: utf-8 -*-
# @author: beauge_z

import pygame

from referee import Referee

def r_false(coord_x=0, coord_y=0):
    _ = coord_x, coord_y
    return False

def r_true(coord_x=0, coord_y=0):
    _ = coord_x, coord_y
    return True

def update_stone_player(screen, player_color):
    coord_x, coord_y = pygame.mouse.get_pos()
    white = pygame.image.load('./img/stoneW.png').convert_alpha()
    black = pygame.image.load('./img/stoneB.png').convert_alpha()
    coord_x = int((coord_x - 5) / 40) * 40 + 5
    coord_y = int((coord_y - 5) / 40) * 40 + 5
    screen.blit(white if player_color == 'w' else black, (round(coord_x), round(coord_y)))

def display_board(screen, board):
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
    run = True
    board = list()
    for cpt_y in range(0, 19):
        to_append = list()
        for cpt_x in range(0, 19):
            to_append.append(None)
        board.append(to_append)
    while run:
        display_board(screen, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        pygame.display.update()
    return True

def load_p_vs_p(screen):
    run = True
    board = list()
    player_color = 'b'
    other = 'w'
    ref = Referee()
    for cpt_y in range(0, 19):
        to_append = list()
        for cpt_x in range(0, 19):
            to_append.append(None)
        board.append(to_append)
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
                rboard = ref.set_stone(board, player_color, [coord_y, coord_x])
                if rboard is not None:
                    board = rboard
                    win = ref.check5(board, [int((coord_y-5)/40), int((coord_x-5)/40)], player_color)
                    score, board = ref.capture(board, [int((coord_y-5)/40), int((coord_x-5)/40)], player_color, other)
                    player_color, other, run = ref.display_score(score, player_color, other, win)
        update_stone_player(screen, player_color)
        pygame.display.update()
    return True
