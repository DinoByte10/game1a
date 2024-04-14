import pygame
import random

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(2, 4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(50, 255), random.randrange(50, 255), random.randrange(50, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.rect.x = random.randrange(0, 800)
        self.rect.y = 0
        self.vel_y = random.randrange(4, 15)
        self.firsty = self.rect.y
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.y > 1000:
            self.rect.y = 0
            self.rect.x = random.randrange(0, 800)
    
