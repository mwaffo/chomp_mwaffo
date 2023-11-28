# a pygame sprite class for a fish

import pygame
import random

MIN_SPEED = 0.5
MAX_SPEED = 5


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, motion='forward'):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/green_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.motion = motion
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)

        if self.motion == 'backward':
            self.image = pygame.transform.flip(self.image, True, False)

            # scale image if you need by getting current size
            size = self.image.get_size()  # this extract image size as a 2D tuple
            # and multiplying by scale to get desired size
            scale = 0.1
            # scaling up to desired size
            self.image = pygame.transform.scale(self.image, (size[0] * scale, size[1]* scale))

            self.speed = - random.uniform(MIN_SPEED, MAX_SPEED)

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)


fishes = pygame.sprite.Group()