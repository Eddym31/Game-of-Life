import pygame
import numpy as np

pygame.init()

BACKGROUND_COLOR = (5, 5, 5)
WIDTH, HEIGHT = 1000, 500
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CELL_SIZE = 20
pygame.display.set_caption("Game of Life")
FPS = 60


class game_of_life:


    def __init__(self, surface, width=1000, height=500, cell_size=20,
                 active_color=(190, 230, 150), inactive_color=(5, 5, 5)):
        """Constructor for the game_of_life class."""

        self.surface = surface
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.active_color = active_color
        self.inactive_color = inactive_color

        self.columns = int(height / cell_size)
        self.rows = int(width / cell_size)

        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def draw_grid(self):
        """Draw the grid of cells on the game surface."""

        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    pygame.draw.rect(self.surface, self.active_color, [row * self.cell_size, col * self.cell_size,
                                                                        self.cell_size - self.cell_size // 10,
                                                                        self.cell_size - self.cell_size // 10])
                else:
                    pygame.draw.rect(self.surface, self.inactive_color, [row * self.cell_size, col * self.cell_size,
                                                                          self.cell_size - self.cell_size // 10,
                                                                          self.cell_size - self.cell_size // 10])

    def update_grid(self):
        """ Update the grid of cells based on the rules of the Game of Life."""

        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_cell(row, col)
        self.grid = updated_grid

    def update_cell(self, x, y):
        """Determines the new state of a cell according to the rules of the game of life.
        :param x: The row of the cell.
        :param y: The column of the cell.
        :return: The new state of the cell (True for alive, False for dead)."""
        
        current_state = self.grid[x, y]
        alive_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if i == 0 and j == 0:
                        continue
                    elif self.grid[x + i, y + j]:
                        alive_neighbors += 1
                except:
                    continue
        if current_state and alive_neighbors < 2:
            return False
        elif current_state and (alive_neighbors == 2 or alive_neighbors == 3):
            return True
        elif current_state and alive_neighbors > 3:
            return False
        elif not current_state and alive_neighbors == 3:
            return True
        else:
            return current_state

    def run(self):
        """Runs the game loop for the game of life."""
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.surface.fill(BACKGROUND_COLOR)
            self.draw_grid()
            self.update_grid()
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = game_of_life(GAME_WINDOW)
    game.run()
