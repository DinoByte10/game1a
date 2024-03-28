import pygame
from bullet import Bullet

class hero_image(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, mx, my):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey((0,0,0))
        self.x = x
        self.y = y
        self.mx = mx
        self.my = my
        self.bullets = []
    def update(self):
        self.x += self.mx
        self.y += self.my
        if self.x > 760:
            self.mx = -0.3
        if self.x < 15:
            self.mx = 0.3
        for b in self.bullets:
            b.update()
    def right(self):
        self.mx += 0.1
    def left(self):
        self.mx -= 0.1
    def shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.x
        new_bullet.rect.y = self.y
        self.bullets.append(new_bullet)