import pygame
from sys import exit
from Map.Tankstelle import Tankstelle
from player.Player import *

pygame.init()

screen = pygame.display.set_mode((1260, 920))
clock = pygame.time.Clock()
pygame.display.set_caption("Truckspiel")


#########PLAYER SETTINGS####################
player_surf = pygame.image.load("player/car-truck4.png").convert_alpha()
player_rect = player_surf.get_rect()
playerspeed = 3

#########Truck Settings###################
# tankstelle = Tankstelle(5000, 800, 100)
tank_surf = pygame.image.load("Map\gasstation.png").convert_alpha()
tank_rect = tank_surf.get_rect(midbottom=(800, 50))


def truck(player_rect):
    screen.blit(player_surf, player_rect)


def tankedraw():
    screen.blit(tank_surf, tank_rect)


# tankstelle.tankstelle_surface(), (tankstelle.getPosX(), tankstelle.getPosY())


def game_loop():
    crashed = False

    while not crashed:
        x_change = 0
        y_change = 0
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
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

        player_rect.x += x_change
        player_rect.y += y_change

        if player_rect.colliderect(tank_rect):
            print(player_rect.colliderect(tank_rect))
        print(player_rect.colliderect(tank_rect))
        screen.fill((255, 255, 255))
        truck(player_rect)
        tankedraw()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
exit()
