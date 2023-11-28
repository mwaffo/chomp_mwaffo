import pygame
import sys
from player import Player

pygame.init()

screen_width = 800
screen_height = 600
tile_size = 64

# clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frogger")

def draw_background(screen):
    grass = pygame.image.load("../carmenfrog/photo/Grass.png").convert()
    water = pygame.image.load("../carmenfrog/photo/Water.jpg").convert()
    # frog = pygame.image.load("../carmenfrog//photo/newfrog.png").convert()

    grass.set_colorkey((0,0,0))
    water.set_colorkey((0,0,0))
    # frog.set_colorkey((0,0,0))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(grass, (x, y))
    for x in range(0, screen_width, tile_size):
        screen.blit(water, (x, screen_height - 400))

background = screen.copy()
draw_background(background)

player = Player(screen_width/2 , screen_height/2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

    # screen.blit(screen, (0, 0)) # avoid this line of code as you are stacking image on top of the previous screen each time resulting into the problem you have
    # draw the background
    screen.blit(background, (0, 0)) # with this line of code, you are using the original background image and not the previous screen

    player.update()
    player.draw(screen)

    pygame.display.flip()

    # Limit the frame rate
    # clock.tick(60)

pygame.quit()
sys.exit()