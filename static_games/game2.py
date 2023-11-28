import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
tile_size = 64
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

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
        screen.blit(sand, (x, screen_height-tile_size))
    # distribute seagrass randomly across the sand, and not too close to the top
    for _ in range(5):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x, screen_height-tile_size*2+20))



# Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background
    screen.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
