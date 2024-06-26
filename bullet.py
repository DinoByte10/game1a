import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        self.width = 5
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (160, 255, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.my = -7

    def update(self):
        self.rect.y += self.my

    