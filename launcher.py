#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: beauge_z

import sys
from options import *
import gameplay

import pygame

class Launcher:
    """
    Class allowing pygame to load.
    """
    pygame.init()
    pygame.display.set_caption('Gomoku')
    pygame.display.set_icon(pygame.image.load('./img/ico.png'))
    def __init__(self):
        self.font = pygame.font.Font('./font/electroharmonix.ttf', 40)
        self.screen = pygame.display.set_mode((770, 770))
        self.options = [Option("Player VS Player", (750, 430), self.font, self.screen, gameplay.loadPvP),
                        Option("Player VS IA", (750, 480), self.font, self.screen, gameplay.loadPvAI),
                        Option("Quit", (750, 750), self.font, self.screen, gameplay.rFalse)]

    def launch(self):
        run = True
        while run:
            pygame.event.pump()
            bg = pygame.image.load('./img/MenuBG.jpg')
            self.screen.blit(bg, (0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        run = False
                for option in self.options:
                    if option.surf.collidepoint(pygame.mouse.get_pos()):
                        option.hover = True
                        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                            run = option.func(self.screen, self.font)
                    else:
                        option.hover = False
                    option.draw()
            for option in self.options:
                if option.surf.collidepoint(pygame.mouse.get_pos()):
                    option.hover = True
                else:
                    option.hover = False
                option.draw()
            pygame.display.update()
        pygame.quit()
        return (0)

if __name__ == '__main__':
    game = Launcher()
    sys.exit(game.launch())
