# To write a Pygame script where the player can shoot bullets in any direction indicated by a mouse click, we need to:
# 1. Initialize Pygame and create a game window
# 2. Load or create a player sprite and bullet sprite
# 3. Capture mouse click events and determine the direction for the bullet to travel
# 4. Update the bullet's position in the direction of the click
# 5. Draw the player, bullets, and other game elements to the screen

# Here is a basic example of how such a script could look:

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooting Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_pos = [width // 2, height // 2]
player_size = 50
player_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
pygame.draw.circle(player_surface, WHITE, (player_size // 2, player_size // 2), player_size // 2)

# Set up the bullet
bullet_size = 10
bullet_surface = pygame.Surface((bullet_size, bullet_size), pygame.SRCALPHA)
pygame.draw.circle(bullet_surface, WHITE, (bullet_size // 2, bullet_size // 2), bullet_size // 2)

# Bullet list
bullets = []

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shooting bullets
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            bullet_dx = mouse_x - player_pos[0]
            bullet_dy = mouse_y - player_pos[1]
            angle = math.atan2(bullet_dy, bullet_dx)
            bullet_speed = 5
            bullets.append(
                [player_pos[0], player_pos[1], bullet_speed * math.cos(angle), bullet_speed * math.sin(angle)])

    # Update bullet positions
    for bullet in bullets:
        bullet[0] += bullet[2]
        bullet[1] += bullet[3]

        # Remove bullets when they leave the screen
        if bullet[0] < 0 or bullet[0] > width or bullet[1] < 0 or bullet[1] > height:
            bullets.remove(bullet)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the player
    screen.blit(player_surface, player_pos)

    # Draw the bullets
    for bullet in bullets:
        screen.blit(bullet_surface, (bullet[0], bullet[1]))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
