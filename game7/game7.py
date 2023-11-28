import pygame
import sys
from fish import fishes
from enemy import enemies
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish, add_enemies

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding Enemies")
# Load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")
life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0, 0, 0))
clock = pygame.time.Clock()

# Main loop
running = True
background = screen.copy()
draw_background(background)

# add the fish, enemies, and player
add_fish(5)
add_enemies(3)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# initialize score and a custom font to display it
score = 0
lives = NUM_LIVES
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

while lives > 0:
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

    # update game objects
    fishes.update()
    enemies.update()
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

    # check for collisions between player and enemy fish
    # remove fish if there is a collision and reduce the
    # number of lives
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        lives -= len(result)
        # play chomp sound
        pygame.mixer.Sound.play(hurt)
        # add new fish
        add_enemies(len(result))

    # if any fish have moved off the left side of the screen, remove them
    # and add a new fish off the right side of the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            add_fish(1)

    # if any enemies have moved off the left side of the screen, remove them
    # and add a new enemy off the right side of the screen
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            add_enemies(1)

    # draw the background
    screen.blit(background, (0, 0))

    # draw game objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    # draw the score in the upper left corner
    message = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(message, (SCREEN_WIDTH - message.get_width() - 10, 0))

    # draw the lives in the lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

screen.blit(background, (0, 0))

# show a game over message
message = score_font.render("Game Over", True, (0, 0, 0))
screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 - message.get_height() / 2))
# show the final score
score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2,
                         SCREEN_HEIGHT / 2 + message.get_height()))
pygame.display.flip()

# play game over sound effect
pygame.mixer.Sound.play(bubbles)

# wait for user to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame
            pygame.quit()
            sys.exit()
