#
#   ALICE CUTLER
#   SOHA PATEL
#   CS 5410
#   MAZE GAME
#
#------------------------------------------------------------------------------

import pygame, random

# setting global variables for the game display
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# --------------------- Classes that Build The Maze ---------------------------

# the maze is built with cells
class Cell():
    width, height = 16, 16

    def __init__(self, x, y, maze):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((BLACK))
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


class Wall(Cell):
    def __init__(self, x, y, maze):
        super(Wall, self).__init__(x, y, maze)
        self.image.fill((WHITE))
        self.type = 0


class Maze:
    def __init__(self, size):
        self.width, self.height = size[0] // Cell.width, size[1] // Cell.height
        self.grid = [[Wall(x, y, self) for y in range(self.height)] for x in range(self.width)]

    def get(self, x, y):
        return self.grid[x][y]

    def build_wall(self, x, y):
        self.grid[x][y] = Wall(x, y, self)

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw_cell(screen)

    #TODO will implement prim's algorithm to generate maze
    def generate(self, screen=None, animate=False):
        # Cells that can become passages (odd coordinates)
        passages = {(x, y) for x in range(1, self.width, 2)
                            for y in range(1, self.height, 2)}

        # Pick a random starting cell
        sx, sy = random.choice(list(passages))
        passages.remove((sx, sy))
        self.grid[sx][sy] = Cell(sx, sy, self)

        # Frontier list: (from_x, from_y, to_x, to_y)
        frontier = []

        def add_frontier(x, y):
            for nx, ny in self.get(x, y).nbs:
                if (nx, ny) in passages:
                    frontier.append((x, y, nx, ny))

        add_frontier(sx, sy)

        while frontier:
            fx, fy, tx, ty = random.choice(frontier)
            frontier.remove((fx, fy, tx, ty))

            # Skip if already carved
            if (tx, ty) not in passages:
                continue

            passages.remove((tx, ty))

            # Carve the destination cell
            self.grid[tx][ty] = Cell(tx, ty, self)

            # Remove the wall between the two cells
            wx = (fx + tx) // 2
            wy = (fy + ty) // 2
            self.grid[wx][wy] = Cell(wx, wy, self)

            # Add new frontier walls
            add_frontier(tx, ty)

            if animate:
                self.draw(screen)
                pygame.display.update()
                pygame.time.wait(10)

# --------------------- Functions that Run the Game ---------------------------

def draw_maze(display_surface):
    maze = Maze((WINDOW_WIDTH, WINDOW_HEIGHT))
    maze.generate(display_surface, animate=True)

def main():
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("*~~~* our aMAZEing game *~~~*")

    # Set game clock and events
    clock = pygame.time.Clock()
    draw_maze(display_surface)
    running = True

    # main game loop
    while running:

        # handle game events
        for event in pygame.event.get():
            # let player quit the game
            if event.type == pygame.QUIT:
                running = False

        # update display
        pygame.display.flip()

        # framerate to 60 FPS
        clock.tick(60)


if __name__ == "__main__":
    main()