import os
import pygame
from pygame import time
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
# from pygame.sprite import Bullet
from bullet import Bullet
from hero import hero_image
from enemy import Enemy
from bg import BG



class Gamec():
    def __init__(self):
        self.bg = BG()
        self.level = 1
        pygame.init()
        pygame.display.set_caption("My game")
        self.screen = pygame.display.set_mode((800, 1000))
        self.clock = pygame.time.Clock()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(current_dir, "hero1.pcx")

        self.enemy_image_path = os.path.join(current_dir, "alien0.pcx")

        self.screen.set_colorkey((0,0,0))

        self.ticks = 60
        
        self.score = 0
        
        self.reset()

        self.font = pygame.font.SysFont(None, 24)

    def reset(self):

        self.last_tick = time.get_ticks()

        self.player = hero_image(self.image_path, 100, 910, 0, 0)

        self.enemies = []

        for r in range(1, self.level + 1):
            for i in range(1, 8):
                self.enemies.append(Enemy(i * 100, r * 100, self.enemy_image_path, self.enemies, i))
    def update_enemies(self):
        for e in self.enemies:
                e.update()
                self.screen.blit(e.image, (e.rect.x, e.rect.y))
                for b in self.player.bullets:
                    if b.rect.x > e.rect.x - 13 and b.rect.x < e.rect.x + 36 and b.rect.y > e.rect.y - 13 and b.rect.y < e.rect.y + 36:
                        self.score += 10 * self.level
                        self.enemies.remove(e)
                        self.player.bullets.remove(b)
                if self.player.x > e.rect.x - 23 and self.player.x < e.rect.x + 26 and self.player.y > e.rect.y - 23 and self.player.y < e.rect.y + 26:
                    # self.enemies.remove(e)
                    self.player.dead = True
    def play(self):
        while True:
            for event in pygame.event.get():
                pass
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT]:
                self.player.right()
            if pressed[pygame.K_LEFT]:
                self.player.left()
            if pressed[pygame.K_ESCAPE]:
                break
            self.screen.fill((0,0,25))
            img = self.font.render(str(self.score), True, pygame.Color(255, 255, 255, 255))
            self.screen.blit(img, (20, 20))
            if pressed[pygame.K_SPACE]:
                if time.get_ticks() - self.last_tick > 360:
                    self.player.shoot()
                    self.last_tick = time.get_ticks()
            self.player.update()
            self.screen.blit(self.player.image, (self.player.x, self.player.y))
            for b in self.player.bullets:
                self.screen.blit(b.image, (b.rect.x, b.rect.y))
            self.update_enemies()
            if len(self.enemies) < 1:
                self.player.win = True
            if self.player.over:
                self.level = 1
                self.reset()
                self.score = 0
            if self.player.complete:
                self.level += 1
                self.reset()
            self.bg.update()
            self.bg.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.ticks)

