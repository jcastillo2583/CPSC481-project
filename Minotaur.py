import pygame
from maze import Maze, Cell

class Minotaur:

    def __init__(self, maze, x, y):
        self.maze = maze
        self.x = x
        self.y = y

    def render(self, surface):
        """**SPAWN AT 0,0"""

        self.x = 0
        self.y = 0

        # l & w of rect = rec length - ( rect width * 2)
        """" If current is on ROW 0 --> rectangle vertical Padding = maze. ver_Padding + rect_Width  """
        if self.x == 0:
            y_start = self.maze.ver_padd + self.maze.rect_width
        else:
            y_start = self.maze.ver_padd + self.y * self.maze.rect_length

        """If current is on COL 0 --> rect horizontal padding = maze.hori_padding + rect_Width"""
        if self.y == 0:
            x_start = self.maze.hori_padd + self.maze.rect_width
        else:
            x_start = self.maze.hori_padd + self.x * self.maze.rect_length

        pygame.draw.rect(surface, (255, 0, 255), (x_start, y_start, self.maze.rect_length-(self.maze.rect_width*2), self.maze.rect_length-(self.maze.rect_width*2)))







  #  def bfs(self, x,y):
        """ use from slides"""
