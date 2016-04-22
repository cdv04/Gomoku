#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: beauge_z

import sys
from options import *

import pygame

def mNone(x=0, y=0):
    return(False, False)

def mResume(x=0, y=0):
    return (True, False)

def mQuit(x=0, y=0):
    return (False, True)

def rFalse(x=0, y=0):
    return False

def rTrue(x=0, y=0):
    return True

def paused(screen, font):
    resume = False
    xquit = False
    options = [Option("Paused", (450, 320), font, screen, mNone),
               Option("Resume", (180, 480), font, screen, mResume),
               Option("Quit", (730, 480), font, screen, mQuit)]
    while not (resume or xquit):
        pygame.draw.rect(screen, (255, 255, 255), (0, 275, 750, 200))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                resume = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    resume = False
            for option in options:
                if option.surf.collidepoint(pygame.mouse.get_pos()):
                    option.hover = True
                    if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                        resume, xquit = option.func()
                        print(not(resume or xquit))
                else:
                    option.hover = False
                option.draw()
        print('->', not(resume or xquit))
        for option in options:
            if option.surf.collidepoint(pygame.mouse.get_pos()):
                option.hover = True
            else:
                option.hover = False
            option.draw()
        pygame.display.update()
        pygame.time.Clock().tick(60)
    return (resume)

def loadPvAI(screen, font):
    run = True
    board = list()
    for j in range(0, 19):
        a = list()
        for i in range(0, 19):
            a.append(None)
        board.append(a)
    while run:
        bg = pygame.image.load('./img/Goban.jpg')
        screen.blit(bg, (0,0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    run = False
        pygame.display.update()
    return True

def loadPvP(screen, font):
    run = True
    board = list()
    playerColor = 'b'
    for j in range(0, 19):
        a = list()
        for i in range(0, 19):
            a.append(None)
        board.append(a)
    while run:
        bg = pygame.image.load('./img/Goban.jpg')
        w = pygame.image.load('./img/stoneW.png').convert_alpha()
        b = pygame.image.load('./img/stoneB.png').convert_alpha()
        screen.blit(bg, (0,0))
        for j in range(0,19):
            for i in range(0,19):
                x = j*(35+5)+5
                y = i*(35+5)+5
                if (board[j][i] == 'b'):
                    screen.blit(b, (round(x), round(y)))
                elif (board[j][i] == 'w'):
                    screen.blit(w, (round(x), round(y)))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    run = False
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                if (board[int((x-5)/40)][int((y-5)/40)] == None):
                    board[int((x-5)/40)][int((y-5)/40)] = playerColor
                    playerColor = 'w' if playerColor == 'b' else 'b'
        x, y = pygame.mouse.get_pos()
        x = int((x-5)/40)*(35+5)+5
        y = int((y-5)/40)*(35+5)+5
        screen.blit(w if playerColor == 'w' else b, (round(x), round(y)))
        pygame.display.update()
    return True
