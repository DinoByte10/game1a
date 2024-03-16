import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

pygame.init()
pygame.display.set_caption("My game")
screen=pygame.display.set_mode((1024, 768))
clock=pygame.time.Clock()

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "hero1.pcx")
hero_image = pygame.image.load(image_path)

screen.set_colorkey((0,0,0))
hero_image.set_colorkey((0,0,0))
ticks=60
x=100
X=0
while True:
    for event in pygame.event.get():
        print(event)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        X += 0.3
    if pressed[pygame.K_LEFT]:
        X -= 0.3
    if pressed[pygame.K_ESCAPE]:
        break
    screen.fill((255,100,0))
    x += X
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, 230, 60, 60))
    #rotated = pygame.transform.rotate(car_image, car.angle)
    rect = hero_image.get_rect()
    screen.blit(hero_image, (x, 30))
    pygame.display.flip()
    clock.tick(ticks)

print("Game Over!")



