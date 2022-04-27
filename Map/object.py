import pygame


class object(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "tankstelle":
            self.image = pygame.image.load("Map\gasstation.png").convert_alpha()
            xpos = 800
            ypos = 50
        else:  # erzlager/depot
            pass
        self.rect = self.image.get_rect(midbottom=(xpos, ypos))
