import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player/car-truck4.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200, 300))

    def player_input(self):
        keys = pygame.key.get_pressed()
        playerspeed = 3
        y_change = 0
        x_change = 0
        if keys[pygame.K_w] & keys[pygame.K_a]:
            y_change = -playerspeed
            x_change = -playerspeed
        if keys[pygame.K_w] & keys[pygame.K_d]:
            y_change = -playerspeed
            x_change = playerspeed
        if keys[pygame.K_w]:
            y_change = -playerspeed
        if keys[pygame.K_s] & keys[pygame.K_a]:
            y_change = playerspeed
            x_change = -playerspeed
        if keys[pygame.K_s] & keys[pygame.K_d]:
            y_change = playerspeed
            x_change = playerspeed
        if keys[pygame.K_s]:
            y_change = playerspeed
        if keys[pygame.K_d]:
            x_change += playerspeed
        if keys[pygame.K_a]:
            x_change = -playerspeed

        self.rect.x += x_change
        self.rect.y += y_change

    def update(self):
        self.player_input()
