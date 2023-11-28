import pygame
import sys
import random
from fish import Fish, fishes
from game7.enemy import Enemy, enemies
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish, add_enemies, add_bullets
from bullet import bullets
from math import atan2, pi

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")

chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
clock = pygame.time.Clock()
life_icon = pygame.image.load("../assets/sprites/orange_fish.png").convert()

running = True
background = screen.copy()
draw_background(background)

#placing fish off right side of screen in random positions
add_fish(5)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#initialize score with custom font
score = 0
lives = NUM_LIVES
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)


for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_HEIGHT * 2), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control player with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_SPACE:
                pos = player.rect.midright
                add_bullets(1, pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                #player.x, player.y = pygame.mouse.get_pos()

                #pos = player.rect.midright
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = - atan2(mouse_y - player.y, mouse_x - player.x)
                add_bullets(1, player.rect.center, angle)


#    pygame.mixer.Sound.play(bensound_music)
    # draw the background
    screen.blit(background, (0, 0))

    #update game objects
    fishes.update()
    # enemies.update()
    player.update()
    bullets.update(player)

    for enemy in enemies:
        direction = atan2(player.y - enemy.y, player.x - enemy.x)
        enemy.update(direction)

    if player.rect.x <= 0:
        player.x = 0
    elif player.rect.x >= screen.get_rect().width - player.rect.width:
        player.x = screen.get_rect().width - player.rect.width
    elif player.rect.y <= 0:
        player.y = 0
    elif player.rect.y >= screen.get_rect().height - player.rect.height:
        player.y = screen.get_rect().height - player.rect.height

    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        # lives += len(result)
        #play chomp sound
        pygame.mixer.Sound.play(chomp)
        #add new fish
        add_fish(len(result))

    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        lives -= len(result)
        # play chomp sound
        pygame.mixer.Sound.play(hurt)
        # add new fish
        add_enemies(len(result))

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            add_fish(1)
            #fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE)))

    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            add_enemies(1)

    for bullet in bullets:
        if bullet.rect.x > SCREEN_WIDTH:
            bullets.remove(bullet)

        for enemy in enemies:
            bullet_enemy = pygame.sprite.spritecollide(bullet, enemies, True)
            if bullet_enemy:
                score += len(bullet_enemy)
                enemies.remove(enemy)
                add_enemies(1)
                bullets.remove(bullet)


        for fish in fishes:
            bullet_fish = pygame.sprite.spritecollide(bullet, fishes, True)
            if bullet_fish:
                score -= len(bullet_fish)
                fishes.remove(fish)
                add_fish(1)

    screen.blit(background, (0,0))

    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    for bullet in bullets:
        bullet.draw_bullet(screen)

    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    for i in range(lives):
        screen.blit(life_icon, (i* TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    # Update the display
    pygame.display.flip()

    #limit frame rate
    clock.tick(60)

screen.blit(background, (0,0))

message = score_font.render("Game Over", True, (0,0,0))
screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 - message.get_height() / 2))
score_text = score_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2,
                         SCREEN_HEIGHT / 2 + message.get_height()))

pygame.display.flip()

pygame.mixer.Sound.play(bubbles)

# Quit Pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()