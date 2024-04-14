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
        self.dead = False
        self.win = False
        self.over = False
        self.complete = False
        self.rect = self.image.get_rect()
    def update(self):
        if self.dead:
            self.my = 5
        if self.win:
            self.my = -10
        self.x += self.mx
        self.y += self.my
        if self.x > 760:
            self.mx = -0.3
        if self.x < 15:
            self.mx = 0.3
        for b in self.bullets:
            b.update()
            if b.rect.y < 0:
                self.bullets.remove(b)
        if self.y > 1100:
            self.over = True
        if self.y < 0:
            self.complete = True
    def right(self):
        self.mx += 0.1
    def left(self):
        self.mx -= 0.1
    def shoot(self):
        if len(self.bullets) > 3 or self.dead or self.over:
            return
        new_bullet = Bullet()
        new_bullet.rect.x = -5 //2 + self.x + self.image.get_width() //2
        new_bullet.rect.y = self.y
        self.bullets.append(new_bullet)
    
