import pygame









class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
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
        self.my = 3
        self.firsty = y
    def update(self):
        self.rect.y += self.my
        print(self.rect.y)
        if self.rect.y > 1000:
            self.rect.y = - 100 - self.firsty





