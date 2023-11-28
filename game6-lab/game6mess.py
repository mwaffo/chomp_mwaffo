import time

import pygame
import sys
import random
from fish import Fish, fishes
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")
# Load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
bensound_music = pygame.mixer.Sound("../assets/sounds/bensound-summer_ogg_music.ogg")
clock = pygame.time.Clock()

# Main loop
running = True
background = screen.copy()
draw_background(background)

# place fish off the right side of the screen in random positions
add_fish(5)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# initialize score and a custom font to display it
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

def draw_welcome(screen):
# draw the title at the top center of the screen
    game_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 64)
    text = game_font.render("Welcome to Chomp", True, (155, 155, 255))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))

draw_mess = True

# # Method 1
# if draw_mess:
#     # draw the background
#     screen.blit(background, (0, 0))
#
#     # welcome message
#     draw_welcome(screen)
#
#     # Update the display
#     pygame.display.flip()
#     time.sleep(5)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control player with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()

    pygame.mixer.Sound.play(bensound_music)
    # draw the background
    screen.blit(background, (0, 0))

    # Method 2
    if draw_mess:
        draw_mess = False

        # welcome message
        draw_welcome(screen)

        # Update the display
        pygame.display.flip()
        time.sleep(5)

    # update game objects
    fishes.update()
    player.update()

    # check for collisions between player and fish
    # update score and remove fish if there is a collision
    # use group collision detection
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        score += len(result)
        # play chomp sound
        pygame.mixer.Sound.play(chomp)
        # add new fish
        add_fish(len(result))

    # if any fish have moved off the left side of the screen, remove them
    # and add a new fish off the right side of the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            add_fish(1)

    # draw game objects
    fishes.draw(screen)
    player.draw(screen)

    # draw the score in the upper left corner
    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    # Update the display
    pygame.display.flip()


    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
