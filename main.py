import pygame
from sys import exit
from Map.object import *
from player.Player import *

pygame.init()

screen = pygame.display.set_mode((1260, 920))
clock = pygame.time.Clock()
pygame.display.set_caption("Truckspiel")


#########PLAYER SETTINGS####################
player = pygame.sprite.GroupSingle()
player.add(Player())


#########Objekt Settings###################
object_group = pygame.sprite.Group()


def game_loop():
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        object_group.add(object("tankstelle"))
        screen.fill((255, 255, 255))
        object_group.draw(screen)
        object_group.update()
        player.draw(screen)
        player.update()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
exit()
