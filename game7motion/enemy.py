# a pygame sprite class for enemy

import pygame
import random
from game_parameters import *
from math import cos, sin


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/puffer_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
        self.rect.center = (x, y)

    def update(self, direction):
        self.x += self.speed * cos(direction)
        self.rect.x = self.x
        self.y += self.speed * sin(direction)
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


enemies = pygame.sprite.Group()
