import pygame
from Map.positions import *


class Tankstelle(Position):
    imgpath = "Map\gasstation.png"

    def __init__(self, spritkapazitat, posx, posy):
        self.spritkapazitat = spritkapazitat
        self.setPosX(posx)
        self.setPosY(posy)

    def tanken(self):
        self.spritkapazitat = self.spritkapazitat - 10

    def tankstelle_surface(self):
        return pygame.image.load(self.imgpath)
