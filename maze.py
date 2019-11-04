import pygame
import random

# Create a maze using the depth-first algorithm described at
# https://scipython.com/blog/making-a-maze/
# Christian Hill, April 2017.

class Cell:
    """A cell in the maze.

    A maze "Cell" is a point in the grid which may be surrounded by walls to
    the north, east, south or west.

    """

    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""

        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def has_all_walls(self):
        """Does this cell still have all its walls?"""

        return all(self.walls.values())

    def knock_down_wall(self, other, wall):
        """Knock down the wall between cells self and other."""

        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

class Maze:
    """A Maze, represented as a grid of cells."""

    def __init__(self, nx, ny, ix=0, iy=0):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).

        """

        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]

    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""

        return self.maze_map[x][y]

    def __str__(self):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * self.nx*2]
        for y in range(self.ny):
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def render(self,surface, hori_padd=456, ver_padd=10):
        rect_length = (surface.get_width()-hori_padd*2)/self.nx
        rect_width = abs((rect_length*self.ny-surface.get_height()-ver_padd*2)/(self.ny-1))
        print("Calculated width is: " + str(rect_width))
        x_pos = hori_padd
        y_pos = ver_padd
        for y in range(self.ny):
            for x in range(self.nx):
                if(self.maze_map[x][y].walls['N']):
                    pygame.draw.rect(surface, (255,0,0), (x_pos, y_pos, rect_length ,rect_width))
                    pygame.display.update()
                if(self.maze_map[x][y].walls['E']):
                    pygame.draw.rect(surface, (0,255,0), (x_pos+rect_length-rect_width, y_pos, rect_width,rect_length))
                    pygame.display.update()
                if(self.maze_map[x][y].walls['S']):
                    pygame.draw.rect(surface, (255,0,255), (x_pos, y_pos+rect_length-rect_width, rect_length,rect_width))
                    pygame.display.update()
                if(self.maze_map[x][y].walls['W']):
                    pygame.draw.rect(surface, (255,255,0), (x_pos, y_pos, rect_width,rect_length))
                    pygame.display.update()
                x_pos = x_pos + rect_length- rect_width
            ###Move the y coordinate y +length
            y_pos = y_pos + rect_length - rect_width
            x_pos = hori_padd

            #End Inner For
        #End Outer For


    def find_valid_neighbours(self, cell):
        delta = [('W', (-1,0)),
                 ('E', (1,0)),
                 ('S', (0,1)),
                 ('N', (0,-1))]
        neighbours = []
        for direction, (dx,dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def make_maze_step(self, surface ):
        # Total number of cells.
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            self.render(surface)
            pygame.time.delay(1000)
            surface.fill((0,0,0))
            neighbours = self.find_valid_neighbours(current_cell)
            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue
            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1



    def make_maze(self):
        # Total number of cells.
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.find_valid_neighbours(current_cell)
            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue
            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1
