import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
from bullet import Bullet

pygame.init()
pygame.display.set_caption("My game")
screen=pygame.display.set_mode((1024, 768))
clock=pygame.time.Clock()

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "hero1.pcx")
hero_image = pygame.image.load(image_path)
player = hero_image


screen.set_colorkey((0,0,0))
hero_image.set_colorkey((0,0,0))
ticks=60
x=100
X=0
y=700
Y=0

while True:
    for event in pygame.event.get():
        print(event)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        X += 0.1
    if pressed[pygame.K_LEFT]:
        X -= 0.1
    if pressed[pygame.K_UP]:
        Y -= 0.1
    if pressed[pygame.K_DOWN]:
        Y += 0.1
    if y > 752:
        y = 751
    if y < 700:
        y = 701
    if x > 1010:
        X = -0.3
    if x < 15:
        X = 0.3
    if pressed[pygame.K_ESCAPE]:
        break
    screen.fill((0,0,25))
    
if pressed[pygame.K_SPACE]:
        player.shoot()

class hero_image(pygame.sprite.Sprite):
        def shoot(self):
            new_bullet = Bullet
            new_bullet.rect.x = self.rect.x
            new_bullet.rect.y = self.rect.y
            self.bullets.add(new_bullet)
    
x += X
y += Y




    

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
rect = player.get_rect()
screen.blit(player, (x, y))
pygame.display.flip()
clock.tick(ticks)




print("Game Over!")



