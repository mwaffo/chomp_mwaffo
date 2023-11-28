import pygame
import sys
import random
from fish import Fish, fishes_LR, fishes_RL

# Initialize Pygame
pygame.init()

# Screen dimensions
tile_size = 64
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

clock = pygame.time.Clock()


def draw_background(surf):
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
            surf.blit(water, (x, y))
    # draw the sand top along the bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height - tile_size))
    # distribute seagrass randomly across the sand, and not too close to the top
    for _ in range(5):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x, screen_height - tile_size * 2 + 20))
    # draw the title at the top center of the screen
    custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)
    text = custom_font.render("Chomp", True, (255, 69, 0))
    surf.blit(text, (screen_width / 2 - text.get_width() / 2, 0))


# Main loop
running = True
background = screen.copy()
draw_background(background)
# place fish off the right side of the screen in random positions
for _ in range(5):
    fishes_LR.add(Fish(random.randint(screen_width, screen_width * 2),
                    random.randint(tile_size, screen_height - tile_size)))

# place fish off the left side of the screen in random positions
for _ in range(5):
    fishes_RL.add(Fish(random.randint(-screen_width, 0),
                    random.randint(tile_size, screen_height - tile_size), 'LtoR'))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background
    screen.blit(background, (0, 0))

    # update game objects
    fishes_LR.update()
    fishes_RL.update()

    # if any fish have moved off the left side of the screen, remove them
    # and add a new fish off the right side of the screen
    for fish in fishes_LR:
        if fish.rect.x < -fish.rect.width:
            fishes_LR.remove(fish)
            fishes_LR.add(Fish(screen_width,
                            random.randint(tile_size, screen_height - tile_size)))

    # if any fish have moved off the right side of the screen, remove them
    # and add a new fish off the left side of the screen
    for fish in fishes_RL:
        if fish.rect.x > screen_width:
            fishes_RL.remove(fish)
            fishes_RL.add(Fish(random.randint(-screen_width, 0),
                    random.randint(tile_size, screen_height - tile_size), 'backward'))

    # draw game objects
    fishes_LR.draw(screen)
    fishes_RL.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
