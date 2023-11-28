import pygame
from game_parameters import *
from math import cos, sin


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
        self.x = x
        self.y = y
        self.angle = angle

    def update(self):
        """Move the bullet up the screen."""
        # Update the position of the bullet.
        self.x += BULLET_SPEED * cos(self.angle)
        self.y -= BULLET_SPEED * sin(self.angle)

        # Update the rect position.
        self.rect.x, self.rect.y = self.x, self.y

    def draw_bullet(self, screen):
        """Draw the bullet to the screen."""
        # pygame.draw.rect(screen, BULLET_COLOR, self.rect)
        pygame.draw.circle(screen, BULLET_COLOR, self.rect.center, 10)


bullets = pygame.sprite.Group()
































# if player.x_velocity > 0:
#     self.x += BULLET_SPEED
# elif player.x_velocity < 0:
#     self.x -= BULLET_SPEED
# elif player.y_velocity > 0:
#     self.y -= BULLET_SPEED
# elif player.y_velocity < 0:
#     self.x += BULLET_SPEED


#
# import pygame
# from game_parameters import *
# from math import cos, sin
#
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         # Create a bullet rect at (0, 0) and then set correct position.
#         self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
#         self.x = x
#         self.y = y
#
#         # self.orig_image = pygame.image.load("../assets/sprites/bullets_PNG35491.png").convert()
#         # self.orig_image.set_colorkey((255, 255, 255))
#         #
#         # # scale image if need by getting current size
#         # size = self.orig_image.get_size()  # this extract image size as a 2D tuple
#         # # and multiplying by scale to get desired size
#         # scale = 0.05
#         # # scaling up to desired size
#         # self.orig_image = pygame.transform.scale(self.orig_image, (size[0] * scale, size[1] * scale))
#         #
#         # self.image = self.orig_image
#         # self.rect = self.image.get_rect()
#         # # rect only stores integers, so we keep track of the position separately
#         # self.x = x
#         # self.y = y
#         # self.rect.center = (x, y)
#
#     def update(self, angle):
#         # update image
#         # self.image = self.rot_center(angle)
#         # self.rect = self.image.get_rect()
#
#         """Move the bullet up the screen."""
#         # Update the position of the bullet.
#         self.x += BULLET_SPEED * cos(angle)
#         self.y -= BULLET_SPEED * sin(angle)
#
#         # Update the rect position.
#         self.rect.x, self.rect.y = self.x, self.y
#
#
#     def draw_bullet(self, screen):
#         """Draw the bullet to the screen."""
#         #pygame.draw.rect(screen, BULLET_COLOR, self.rect)
#         pygame.draw.circle(screen, BULLET_COLOR, self.rect.center, 5)
#
#     # def draw_bullet(self, screen):
#     #     screen.blit(self.image, self.rect)
#
#     # def rot_center(self, angle):
#     #     """rotate an image while keeping its center and size"""
#     #     orig_rect = self.orig_image.get_rect() # always rotate the original image
#     #     rot_image = pygame.transform.rotate(self.orig_image, angle)
#     #     rot_rect = orig_rect.copy()
#     #     rot_rect.center = rot_image.get_rect().center
#     #     rot_image = rot_image.subsurface(rot_rect).copy()
#     #     return rot_image
#
#
# bullets = pygame.sprite.Group()


# if player.x_velocity > 0:
#     self.x += BULLET_SPEED
# elif player.x_velocity < 0:
#     self.x -= BULLET_SPEED
# elif player.y_velocity > 0:
#     self.y -= BULLET_SPEED
# elif player.y_velocity < 0:
#     self.x += BULLET_SPEED
