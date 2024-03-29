import os
import pygame
from pygame import time
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
# from pygame.sprite import Bullet
from bullet import Bullet
from hero import hero_image
from enemy import Enemy



class Gamec():
    def __init__(self):
        self.level = 1
        pygame.init()
        pygame.display.set_caption("My game")
        self.screen = pygame.display.set_mode((800, 1000))
        self.clock = pygame.time.Clock()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(current_dir, "hero1.pcx")

        self.enemy_image_path = self.image_path

        self.screen.set_colorkey((0,0,0))

        self.ticks = 60

        self.reset()

    def reset(self):

        self.last_tick = time.get_ticks()

        self.player = hero_image(self.image_path, 100, 910, 0, 0)

        self.enemies = []

        for r in range(1, self.level + 1):
            for i in range(1, 8):
                self.enemies.append(Enemy(i * 100, r * 100, self.enemy_image_path))
    def play(self):
        while True:
            for event in pygame.event.get():
                print(event)
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT]:
                self.player.right()
            if pressed[pygame.K_LEFT]:
                self.player.left()
            if pressed[pygame.K_ESCAPE]:
                break
            self.screen.fill((0,0,25))
            print(self.last_tick, time.get_ticks)
            if pressed[pygame.K_SPACE]:
                if time.get_ticks() - self.last_tick > 360:
                    self.player.shoot()
                    self.last_tick = time.get_ticks()
            self.player.update()
            self.screen.blit(self.player.image, (self.player.x, self.player.y))
            for b in self.player.bullets:
                self.screen.blit(b.image, (b.rect.x, b.rect.y))
            for e in self.enemies:
                e.update()
                self.screen.blit(e.image, (e.rect.x, e.rect.y))
                for b in self.player.bullets:
                    if b.rect.x > e.rect.x - 13 and b.rect.x < e.rect.x + 36 and b.rect.y > e.rect.y - 13 and b.rect.y < e.rect.y + 36:
                        self.enemies.remove(e)
                        self.player.bullets.remove(b)
                if self.player.x > e.rect.x - 13 and self.player.x < e.rect.x + 36 and self.player.y > e.rect.y - 13 and self.player.y < e.rect.y + 36:
                    self.enemies.remove(e)
                    self.player.dead = True
            if len(self.enemies) < 1:
                self.player.win = True
            pygame.display.flip()
            self.clock.tick(self.ticks)
            if self.player.over:
                self.level = 1
                self.reset()
            if self.player.complete:
                self.level += 1
                self.reset()

