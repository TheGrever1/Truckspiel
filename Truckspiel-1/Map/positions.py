import pygame


class Position:
    def __init__(self, posx, posy, width, heigth):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.heigth = heigth

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def setPosX(self, posx):
        self.posx = posx

    def setPosY(self, posy):
        self.posy = posy
