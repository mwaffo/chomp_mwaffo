# Pygame script for a basic game where the player can shoot bullets in any direction indicated by a mouse click

import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player settings
player_pos = [screen_width // 2, screen_height // 2]
player_size = 50

# Bullet settings
bullet_speed = 10
bullets = []  # Store bullets as dictionaries for position and direction

# Clock for controlling frame rate
clock = pygame.time.Clock()

def draw_player(position):
    pygame.draw.rect(screen, RED, (position[0], position[1], player_size, player_size))

def fire_bullet(position, direction):
    bullets.append({"position": list(position), "direction": direction})

def update_bullet_positions():
    for bullet in bullets:
        # Update bullet position based on its direction
        bullet["position"][0] += bullet_speed * math.cos(bullet["direction"])
        bullet["position"][1] += bullet_speed * math.sin(bullet["direction"])

        # Remove bullets that go off screen
        if bullet["position"][0] < 0 or bullet["position"][0] > screen_width or \
           bullet["position"][1] < 0 or bullet["position"][1] > screen_height:
            bullets.remove(bullet)

def draw_bullets():
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, bullet["position"], 5)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position and calculate angle for bullet direction
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - player_pos[1], mouse_x - player_pos[0])
            fire_bullet(player_pos, angle)

    update_bullet_positions()
    draw_player(player_pos)
    draw_bullets()

    pygame.display.flip()  # Update screen
    clock.tick(30)  # 30 frames per second

pygame.quit()
