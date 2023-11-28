import pygame
import random

from fish import Fish, fishes
from game_parameters import *
from enemy import Enemy, enemies
from bullet import Bullet, bullets
from math import atan2


def draw_background(screen):
    # Load tiles from the assets folder into surfaces
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    # use the png transparency
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    # fill the screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x, y))

    # draw the sand top along the bottom
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x, screen_height - tile_size))

    # distribute seagrass randomly across the sand, and not too close to the top
    for _ in range(5):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x, screen_height - tile_size * 2 + 20))

    # Load Game Font
    custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 128)
    # create a text object with the message "Chomp" to display, and the tuple (255, 69, 0) as the font color
    text = custom_font.render("Chomp", True, (255, 69, 0))
    # Draw the text
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 0))


def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(screen_width, screen_width * 2),
                        random.randint(tile_size, screen_height - tile_size)))


def add_enemies(num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(screen_width, screen_width * 2),
                          random.randint(tile_size, screen_height - tile_size)))


def add_bullets(num_bullets, pos, angle):
    for _ in range(num_bullets):
        bullets.add(Bullet(pos[0], pos[1], angle))
