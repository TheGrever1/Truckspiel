import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image(color)
        self.rect = self.image.get_rect()

    def getrect(self):
        return self.rect
