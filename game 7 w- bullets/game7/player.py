import pygame
import sys
import random
from fish import Fish,fishes
from game_parameters import *
from utilities import draw_background
import random


#MIN_SPEED = 0.5
#MAX_SPEED = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()

        self.forward_image = pygame.image.load("../assets/sprites/orange_fish.png").convert()
        self.forward_image.set_colorkey((0,0,0))

        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)

        self.image = self.forward_image
        self.rect = self.image.get_rect()
        # rect only stores integers, so we keep track of the postiton seperately
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_velocity = 0
        self.y_velocity = 0

    def move_up(self):
            self.y_velocity = - PLAYER_SPEED

    def move_down(self):
            self.y_velocity = PLAYER_SPEED

    def move_left(self):
            self.x_velocity = -1 *PLAYER_SPEED
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


