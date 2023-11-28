# a pygame sprite class for a fish

import pygame
from game_parameters import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load("../assets/sprites/orange_fish.png").convert()
        self.forward_image.set_colorkey((0, 0, 0))

        # scale image if you need by getting current size
        size = self.forward_image.get_size()
        # this extract image size as a 2D tuple and multiplying by scale to get desired size
        scale = 1
        # scaling up to desired size
        self.forward_image = pygame.transform.scale(self.forward_image, (size[0] * scale, size[1] * scale))

        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        # rect only stores integers, so we keep track of the position separately
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_velocity = 0
        self.y_velocity = 0

    # ROTATE CENTER — WIKI - Rotate while keeping an image's center and size
    def rot_center(self, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = self.forward_image.get_rect()
        rot_image = pygame.transform.rotate(self.forward_image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def move_up(self):
        self.y_velocity = - PLAYER_SPEED
        self.image = self.rot_center(90)

    def move_down(self):
        self.y_velocity = PLAYER_SPEED
        self.image = self.rot_center(-90)

    def move_left(self):
        self.x_velocity = -1 * PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_velocity = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
