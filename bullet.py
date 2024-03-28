import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        self.width = 4
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (255,0,0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.my = -7

    def update(self):
        self.rect.y += self.my
        print(self.rect.y)