import pygame
import random

from game_parameters import *
from fish import Fish, fishes
from enemy import Enemy, enemies
from bullet import Bullet, bullets

# player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def draw_background(surf):
    # Load tiles from the assets folder into surfaces
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    # use the png transparency
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))
    # fill the screen with water
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(water, (x, y))
    # draw the sand top along the bottom
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surf.blit(sand, (x, SCREEN_HEIGHT - TILE_SIZE))
    # distribute seagrass randomly across the sand, and not too close to the top
    for _ in range(5):
        x = random.randint(0, SCREEN_WIDTH)
        surf.blit(seagrass, (x, SCREEN_HEIGHT - TILE_SIZE * 2 + 20))
    # draw the title at the top center of the screen
    game_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)
    text = game_font.render("Chomp", True, (255, 69, 0))
    surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))


def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))


def add_enemies(num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
                          random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))


def add_bullets(num_bullets, pos):
    for _ in range(num_bullets):
        bullets.add(Bullet(pos[0],pos[1]))
