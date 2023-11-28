import pygame
import random
from game_parameters import *
from math import cos, tan, sin

ENEMY_MIN_SPEED = 0.5
ENEMY_MAX_SPEED = 3

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super().__init__()

        self.image = pygame.image.load("../assets/sprites/green_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)

        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.center = (x,y)

        self.speed = random.uniform(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)

    def update(self, direction):
        self.x += self.speed * cos(direction)
        self.rect.x = self.x
        self.y += self.speed * sin(direction)
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


enemies = pygame.sprite.Group()
