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

import pathlib
current_directory = str(pathlib.Path(__file__).parent.resolve())

class Gamec():
    def __init__(self):
        f = open(current_directory + "\\score.txt")
        self.highscore = int(f.read())
        print(self.highscore)
        self.bg = BG()
        self.level = 1
        self.lives = 3
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
        


        self.font = pygame.font.SysFont(None, 24)

        self.player = hero_image(self.image_path, 100, 910, 0, 0)
        self.reset()
    def reset(self):
        
        self.player.reset()

        self.last_tick = time.get_ticks()

        self.enemies = []
         
        for r in range(1, self.level + 1):
            for i in range(1, 8):
                self.enemies.append(Enemy(i * 100, r * 100, self.enemy_image_path, self.enemies, i))
    def update_enemies(self):
        for e in self.enemies:
                e.update()
                self.screen.blit(e.image, (e.rect.x, e.rect.y))
                for b in self.player.bullets:
                    if b.rect.x > e.rect.x - 18 and b.rect.x < e.rect.x + 31 and b.rect.y > e.rect.y - 18 and b.rect.y < e.rect.y + 31:
                        self.score += 10 * self.level
                        self.enemies.remove(e)
                        self.player.bullets.remove(b)
                if self.player.x > e.rect.x - 23 and self.player.x < e.rect.x + 26 and self.player.y > e.rect.y - 23 and self.player.y < e.rect.y + 26:
                    # self.enemies.remove(e)
                    self.lives -= 1
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
            img = self.font.render(str(self.player.lives), True, pygame.Color(255, 255, 255, 255))
            self.screen.blit(img, (20, 20))
            img = self.font.render(str(self.score), True, pygame.Color(255, 255, 255, 255))
            self.screen.blit(img, (350, 20))
            if pressed[pygame.K_SPACE]:
                if time.get_ticks() - self.last_tick > 360:
                    self.player.shoot()
                    self.last_tick = time.get_ticks()
            self.player.update()
            self.screen.blit(self.player.image, (self.player.x, self.player.y))
            for b in self.player.bullets:
                self.screen.blit(b.image, (b.rect.x, b.rect.y))
            self.update_enemies()
            if self.player.y > 1100:
                print("death complete")
                self.player.y = self.player.original_y
                self.player.lives -= 1
                self.player.dead = False
                self.player.my = 0
                self.reset()
            if self.player.win:
                print("during win animation")
                self.player.my = -10
            if self.player.lives < 1:
                print("lost all lives")
                self.player.over = True
            if len(self.enemies) < 1:
                print("last enemy killed--> win")
                self.player.win = True
            if self.player.over:
                if self.score > self.highscore:
                    f = open(current_directory + "\\score.txt", "w")
                    # self.highscore = int(f.read())
                    f.write(str(self.score))
                    f.close()
                print("back to level 1")
                self.level = 1
                # self.reset()
                self.score = 0
                self.player = hero_image(self.image_path, 100, 910, 0, 0)
            if self.player.y < 0:
                print("end of animation")
                # self.player.win = False
                self.level += 1
                self.reset()
            self.bg.update()
            self.bg.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.ticks)

