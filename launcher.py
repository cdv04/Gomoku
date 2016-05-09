#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: beauge_z

import sys
import pygame

from options import Option
import gameplay

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
        self.options = [Option("Player VS Player", (750, 430), self.font, self.screen, gameplay.load_p_vs_p),
                        Option("Player VS IA", (750, 480), self.font, self.screen, gameplay.load_p_vs_ai),
                        Option("Quit", (750, 750), self.font, self.screen, gameplay.r_false)]

    def launch(self):
        run = True
        while run:
            pygame.event.pump()
            background = pygame.image.load('./img/MenuBG.jpg')
            self.screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                for option in self.options:
                    if option.surf.collidepoint(pygame.mouse.get_pos()):
                        option.hover = True
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            run = option.func(self.screen)
                    else:
                        option.hover = False
                    option.draw()
            for option in self.options:
                option.hover = bool(option.surf.collidepoint(pygame.mouse.get_pos()))
                option.draw()
            pygame.display.update()

    def exit(self):
        pygame.quit()
        return 0

if __name__ == '__main__':
    __game__ = Launcher()
    __game__.launch()
    sys.exit(__game__.exit())
