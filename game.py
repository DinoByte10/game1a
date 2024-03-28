import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
# from pygame.sprite import Bullet
from bullet import Bullet
from hero import hero_image


pygame.init()
pygame.display.set_caption("My game")
screen=pygame.display.set_mode((800, 1000))
clock=pygame.time.Clock()

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "hero1.pcx")

screen.set_colorkey((0,0,0))

player = hero_image(image_path, 100, 910, 0, 0)

ticks=60

while True:
    for event in pygame.event.get():
        print(event)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        player.right()
    if pressed[pygame.K_LEFT]:
        player.left()
    if pressed[pygame.K_ESCAPE]:
        break
    screen.fill((0,0,25))
    if pressed[pygame.K_SPACE]:
        player.shoot()

    player.update()




    

    pygame.draw.rect(screen, (255,255,255), pygame.Rect(100, 200, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(165, 335, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(195, 375, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(275, 400, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(333, 515, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(345, 580, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(470, 600, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(500, 300, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(480, 275, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(400, 210, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(1000, 600, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(775, 565, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(100, 200, 5, 5))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(100, 200, 5, 5))  
    #rotated = pygame.transform.rotate(car_image, car.angle)
    # rect = player.get_rect()
    screen.blit(player.image, (player.x, player.y))
    for b in player.bullets:
        screen.blit(b.image, (b.rect.x, b.rect.y))
    pygame.display.flip()
    clock.tick(ticks)




print("Game Over!")



