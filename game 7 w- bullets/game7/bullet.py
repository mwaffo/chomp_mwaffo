import pygame
from game_parameters import*
from math import cos, sin

class Bullet (pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.rect = pygame.Rect(0,0, BULLET_WIDTH, BULLET_HEIGHT)
        self.x = x
        self.y = y
        self.angle = angle

    def update(self, player):
        self.x += BULLET_SPEED * cos(self.angle)
        self.y -= BULLET_SPEED * sin(self.angle)
        self.rect.x, self.rect.y = self.x, self.y

    def draw_bullet(self, screen):
        pygame.draw.rect(screen, BULLET_COLOR, self.rect)

bullets = pygame.sprite.Group()