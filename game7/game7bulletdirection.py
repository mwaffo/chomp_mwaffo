import pygame
import sys
from fish import fishes
from enemy import enemies
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish, add_enemies, add_bullets
from bullet import bullets

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding Enemies")
# Load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")
bensound_music = pygame.mixer.Sound("../assets/sounds/bensound-summer_ogg_music.ogg")
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
# add_bullets(5)
# bullets = pygame.sprite.Group()

# def add_bullets(num_bullets):
#     for _ in range(num_bullets):
#         pos = player.rect.midright
#         bullets.add(Bullet(pos[0],pos[1]))

# add_bullets(1)

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

            if event.key == pygame.K_SPACE:
                pos = player.rect.midright
                add_bullets(1, pos)

        # add mouse event https://www.pygame.org/docs/ref/mouse.html
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                player.x, player.y = pygame.mouse.get_pos()

            # elif pygame.mouse.get_pressed()[1]:
            #     rel_x, rel_y = pygame.mouse.get_rel()
            #     player.x_velocity, player.y_velocity = int(0.1*rel_x), int(0.1*rel_y)
            #     player.update()

    # play background music
    pygame.mixer.Sound.play(bensound_music)

    # update game objects
    fishes.update()
    enemies.update()
    player.update()
    bullets.update()

    # make sure player does not exit the screen
    if player.rect.x <= 0:
        player.x = 0
    elif player.rect.x >= screen.get_rect().width - player.rect.width:
        player.x = screen.get_rect().width - player.rect.width
    elif player.rect.y <= 0:
        player.y = 0
    elif player.rect.y >= screen.get_rect().height - player.rect.height:
        player.y = screen.get_rect().height - player.rect.height

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


    # if any fish have moved off the left side of the screen, remove them
    # and add a new fish off the right side of the screen
    for bullet in bullets:

        if bullet.rect.x > SCREEN_WIDTH:
            bullets.remove(bullet)

        for enemy in enemies:
            bullet_enemy = pygame.sprite.spritecollide(bullet, enemies, True)
            if bullet_enemy: # enemy is killed?
                score += len(bullet_enemy) # increment score is you shoot an enemy
                enemies.remove(enemy) # remove the enemy killed
                add_enemies(1) # add new enemy to the game
                bullets.remove(bullet)
                # pos = player.rect.midright
                # add_bullets(1, pos)

        for fish in fishes:
            bullet_fish = pygame.sprite.spritecollide(bullet, fishes, True)
            if bullet_fish:
                score -= len(bullet_fish)  # decrease score if you shoot a friend
                fishes.remove(fish)
                add_fish(1)
                bullets.remove(bullet)
                # pos = player.rect.midright
                # add_bullets(1, pos)

    # draw the background
    screen.blit(background, (0, 0))

    # draw game objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet(screen)
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
