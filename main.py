import pygame
import sys

pygame.init()

display_width = 1080
display_height = 920

truckimagepath = "player/car-truck4.png"
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
speed = 3
truckImg = pygame.image.load(truckimagepath)
pygame.display.set_caption("Truckspiel")


def truck(x, y):
    screen.blit(truckImg, (x, y))


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
            y_change = -speed
            x_change = -speed
        if keys[pygame.K_w] & keys[pygame.K_d]:
            y_change = -speed
            x_change = speed
        if keys[pygame.K_w]:
            y_change = -speed
            pygame.transform.rotate(truckImg, 180)  # funkt bisher nicht
        if keys[pygame.K_s] & keys[pygame.K_a]:
            y_change = speed
            x_change = -speed
        if keys[pygame.K_s] & keys[pygame.K_d]:
            y_change = speed
            x_change = speed
        if keys[pygame.K_s]:
            y_change = speed
        if keys[pygame.K_d]:
            x_change = speed
        if keys[pygame.K_a]:
            x_change = -speed

        x += x_change
        y += y_change
        screen.fill((255, 255, 255))
        truck(x, y)
        pygame.display.update()
        clock.tick(60)


def Tankstelle(posx, posy, width, heigth, color):
    pygame.draw.rect(screen, color, [posx, posy, width, heigth])


game_loop()
pygame.quit()
quit()
