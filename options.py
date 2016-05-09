# -*- coding: utf-8 -*-
# @author: beauge_z

class Option:
    """
    Class for the menu button, with mouse hovering.
    """
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
        self.render = self.mFont.render(self.text, True, self.getColor())
        self.screen.blit(self.render, self.surf)

    def getColor(self):
        if self.hover:
            return (232, 95, 137)
        else:
            return (0, 0, 0)

    def setSurf(self):
        self.render = self.mFont.render(self.text, True, self.getColor())
        self.surf = self.render.get_rect()
        self.surf.bottomright = self.pos
