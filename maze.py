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
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


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
        self.image.fill(WHITE)
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


# --------------------- Classes that define game objects ----------------------


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        # self.image = pygame.Surface([Cell.width, Cell.height])
        # self.image.fill(BLUE)
        self.image = pygame.image.load("assets/mouse-512.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Cell.width, Cell.height))
        self.rect = self.image.get_rect()
        self.rect.x = x * Cell.width
        self.rect.y = y * Cell.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # should only move if the new position is a Cell (not a Wall) and within the maze bounds
    def move(self, dx, dy, maze):
        new_x = self.rect.x // Cell.width + dx
        new_y = self.rect.y // Cell.height + dy

        if 0 <= new_x < maze.width and 0 <= new_y < maze.height:
            if not isinstance(maze.get(new_x, new_y), Wall):
                self.rect.x += dx * Cell.width
                self.rect.y += dy * Cell.height


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Exit, self).__init__()
        # self.image = pygame.Surface([Cell.width, Cell.height])
        # self.image.fill(GREEN)
        self.image = pygame.image.load("assets/exit-256.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Cell.width, Cell.height))
        self.rect = self.image.get_rect()
        self.rect.x = x * Cell.width
        self.rect.y = y * Cell.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# --------------------- Functions that Run the Game ---------------------------    


def main():
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("*~~~* our aMAZEing game *~~~*")

    # Set game clock and events
    clock = pygame.time.Clock()
    maze = Maze((WINDOW_WIDTH, WINDOW_HEIGHT))
    maze.generate(display_surface, animate=False)

    open_cells = [cell for row in maze.grid for cell in row if not isinstance(cell, Wall)]

    # Spawn player
    player_cell = random.choice(open_cells)
    player = Player(player_cell.x, player_cell.y)

    # Remove player's cell from possible exit locations
    exit_cells = [
        cell for cell in open_cells
        if cell != player_cell
    ]

    # Spawn exit
    exit_cell = random.choice(exit_cells)
    exit = Exit(exit_cell.x, exit_cell.y)

    move_delay = 300  # milliseconds
    last_move = 0

    running = True

    # main game loop
    while running:

        # handle game events
        for event in pygame.event.get():

            # update player position based on key presses
            keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()

            if current_time - last_move >= move_delay:
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    player.move(0, -1, maze)

                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    player.move(0, 1, maze)

                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    player.move(-1, 0, maze)

                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    player.move(1, 0, maze)

            # let player quit the game
            if event.type == pygame.QUIT:
                running = False

        # framerate to 60 FPS
        clock.tick(60)

        # update display after events
        pygame.display.update()
        maze.draw(display_surface)
        exit.draw(display_surface)
        player.draw(display_surface)


if __name__ == "__main__":
    main()