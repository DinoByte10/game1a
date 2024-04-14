import pygame
from star import Star
import random

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface((800, 1000))
        self.color = (0, 0, 25)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = range(1, 10)
        for t in self.timer:
            new_star = Star()
            self.stars.add(new_star)
    def update(self):
        self.stars.update()
        self.stars.draw(self.image)


    

