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


# --------------------- Classes that Build The Maze ---------------------------

# the maze is built with cells
class Cell():
    width, height = 16, 16

    def __init__(self, x, y, maze):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.width
        self.rect.y = y * self.height

        self.x = x
        self.y = y
        self.maze = maze
        self.nbs = [(x + nx, y + ny) for nx, ny in ((-2, 0), (0, -2), (2, 0), (0, 2))
                    if 0 <= x + nx < maze.width and 0 <= y + ny < maze.height]

    def draw_cell(self, screen):
        screen.blit(self.image, self.rect)


class Wall():
    def __init__(self, x, y, maze):
        super(Wall, self).__init__(x, y, maze)
        self.image.fill((0, 0, 0))
        self.type = 0

    #TODO
    def get(self):
        return self.type

    #TODO
    def build_wall(self):
        return 0

    #TODO
    def draw(self):
        return 0

    #TODO
    def generate_maze(self):
        return 0

class Maze:
    #TODO
    def __init__(self, size):
        self.width, self.height = size[0] // Cell.width, size[1] // Cell.height
        self.grid = [[Wall(x, y, self) for y in range(self.height)] for x in range(self.width)]

# -----------------------------------------------------------------------------

def draw_maze():
    #TODO
    return 0;

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