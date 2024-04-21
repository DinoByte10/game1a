import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, enemies, row):
        self.row = row
        self.image = pygame.image.load(image_path)
        self.enemies = enemies
        super(Enemy, self).__init__()
        self.width = 25
        self.height = self.width
        self.size = (self.width, self.height)
        #self.image = pygame.Surface(self.size)
        self.color = (160, 255, 255)
        #self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y= -100 - y
        self.my = random.randrange(2, 5)
        self.mx = 0
        self.firsty = y
    def update(self):
        self.rect.y += self.my
        self.rect.x += self.mx
        if self.rect.y > 1000:
            self.rect.y = - 100
            last = 7 if len(self.enemies) >= 8 else len(self.enemies) - 1
            if self.enemies[0] == self or self.enemies[last]== self:
                self.mx = random.randrange(-4, 4)
        if self.rect.x > 800:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = 800
        if self.mx < 0:
            self.my = random.randrange(6, 9)
        if self.mx > 0:
            self.my = random.randrange(6, 9)
                





