#
#   ALICE CUTLER
#   SOHA PATEL
#   CS 5410
#   MAZE GAME
#
#------------------------------------------------------------------------------

import pygame, random

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("*~~~* our aMAZEing game *~~~*")

# Set colors and values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set game clock and events
clock = pygame.time.Clock()
running = True


# main game loop
while running:

    # handle game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # just a blank surface for now
    display_surface.fill(BLACK)

    # update display
    pygame.display.flip()

    # framerate to 60 FPS
    clock.tick(60)


# End the game
pygame.quit()