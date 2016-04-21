#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: beauge_z

import sys, pygame

class Launcher:
    pygame.init()
    pygame.display.set_caption('Gomoku')
    screen = None
    font = pygame.font.Font('./font/electroharmonix.ttf', 40)
    class Option:
        hover = False
        def __init__(self, text, pos, mfont, screen, func):
            self.text = text
            self.pos = pos
            self.mFont = mfont
            self.screen = screen
            self.setSurf()
            self.draw()
            self.func = func
        def draw(self):
            self.getRender()
            self.screen.blit(self.render, self.surf)
        def getRender(self):
            self.render = self.mFont.render(self.text, True, self.getColor())
        def getColor(self):
            if self.hover:
                return (232, 95, 137)
            else:
                return (0, 0, 0)
        def setSurf(self):
            self.getRender()
            self.surf = self.render.get_rect()
            self.surf.bottomright = self.pos

    def loadPvP(self):
        run = True
        while run:
            bg = pygame.image.load('./img/Goban.jpg')
            self.screen.blit(bg, (0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        run = False
            pygame.display.update()
        return True

    def loadPvAI(self):
        run = True
        while run:
            bg = pygame.image.load('./img/Goban.jpg')
            self.screen.blit(bg, (0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        run = False
            pygame.display.update()
        return True

    def mQuit(self):
        return False

    def __init__(self):
        self.screen = pygame.display.set_mode((750, 750))
        self.options = [self.Option("Player VS Player", (730, 430), self.font, self.screen, self.loadPvP),
                        self.Option("Player VS IA", (730, 480), self.font, self.screen, self.loadPvAI),
                        self.Option("Quit", (730, 730), self.font, self.screen, self.mQuit)]
    def launch(self):
        run = True
        while run:
            pygame.event.pump()
            bg = pygame.image.load('./img/MenuBG.JPG')
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
                            run = option.func()
                    else:
                        option.hover = False
                    option.draw()
            for option in self.options:
                if option.surf.collidepoint(pygame.mouse.get_pos()):
                    option.hover = True
                    for e in pygame.event.get():
                        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                            run = option.func()
                else:
                    option.hover = False
                option.draw()
            pygame.display.update()
        pygame.quit()
        return (0)

if __name__ == '__main__':
    game = Launcher()
    sys.exit(game.launch())
