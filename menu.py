#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: beauge_z

import sys, pygame

class Menu:
    pygame.init()
    pygame.display.set_caption('Gomoku')
    screen = None
    font = pygame.font.Font('./font/electroharmonix.ttf', 40)
    class Option:
        hover = False
        def __init__(self, text, pos, mfont, screen):
            self.text = text
            self.pos = pos
            self.mFont = mfont
            self.screen = screen
            self.setSurf()
            self.draw()
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

    def __init__(self):
        self.screen = pygame.display.set_mode((750, 750))
        self.options = [self.Option("Player VS Player", (730, 430), self.font, self.screen),
                        self.Option("Player VS IA", (730, 480), self.font, self.screen),
                        self.Option("Quit", (730, 730), self.font, self.screen)]
        while True:
            pygame.event.pump()
            bg = pygame.image.load('./img/MenuBG.JPG')
            self.screen.blit(bg, (0,0))
            for option in self.options:
                if option.surf.collidepoint(pygame.mouse.get_pos()):
                    option.hover = True
                else:
                    option.hover = False
                option.draw()
            pygame.display.update()
        return (0)

if __name__ == '__main__':
    sys.exit(Menu())
