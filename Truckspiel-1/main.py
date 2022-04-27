import pygame
import sys
from Map.Tankstelle import Tankstelle
from player.Player import *

pygame.init()

display_width = 1080
display_height = 920

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Truckspiel")


#########PLAYER SETTINGS####################
truckimagepath = "player/car-truck4.png"
player = pygame.image.load(truckimagepath)
player_rect = player.get_rect()
playerspeed = 3

#########Truck Settings###################
tankstelle = Tankstelle(5000, 800, 100)


def truck(player_rect):
    screen.blit(player, player_rect)


def tankedraw():
    screen.blit(
        tankstelle.tankstelleimg(), (tankstelle.getPosX(), tankstelle.getPosY())
    )


def game_loop():
    crashed = False
    x = display_width * 0.45
    y = display_height * 0.8

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
            x_change = playerspeed
        if keys[pygame.K_a]:
            x_change = -playerspeed

        player_rect.x += x_change
        player_rect.y += y_change
        screen.fill((255, 255, 255))
        truck(player_rect)
        tankedraw()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
