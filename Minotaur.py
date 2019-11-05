import pygame
import queue
from math import floor, ceil
from maze import Maze, Cell

class Minotaur:

    def __init__(self, surface, maze, x, y):
        self.maze = maze
        self.x = x
        self.y = y
        self.surface = surface

    def render(self, x=0 , y=0):
        #"""**SPAWN AT 0,0"""

        self.x = x
        self.y = y

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

        pygame.draw.rect(self.surface, (255, 0, 255), (ceil(x_start), ceil(y_start), floor(self.maze.rect_length-(self.maze.rect_width*2)), floor(self.maze.rect_length-(self.maze.rect_width*2))))
        pygame.display.update()



    def bfs(self, start, goal):
        queue = []
        traversed = []
        queue.append([{'x': start['x'], 'y': start['y']}])
        #traversed.append({'x' : start['x'], 'y' : start['y']})
        while queue :
            path = queue.pop(0)
            print(path)
            coordinates = path[-1]
            curr_cell = self.maze.maze_map[coordinates['x']][coordinates['y']]
            self.render(path[-1]['x'],path[-1]['y'])
            pygame.display.update()
            if(coordinates == goal):
                return path
            else:
                #If the direction is open, and we havent traversed it yet, and is in the map
                if curr_cell.walls['N'] == False  and {coordinates['x'],coordinates['y']-1} not in traversed and self.maze.is_valid_cell(coordinates['x'],coordinates['y']-1):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x'],'y' : coordinates['y']-1})
                    #traversed.append({'x' : coordinates['x'],'y' : coordinates['y']-1})
                    queue.append(new_path)
                if( curr_cell.walls['E'] == False and {coordinates['x']+1,coordinates['y']} not in traversed and self.maze.is_valid_cell(coordinates['x']+1,coordinates['y'])):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x']+1,'y' : coordinates['y']})
                    #traversed.append({'x' : coordinates['x']+1,'y' : coordinates['y']})
                    queue.append(new_path)
                if( curr_cell.walls['S'] == False and {coordinates['x'],coordinates['y']+1} not in traversed and self.maze.is_valid_cell(coordinates['x'],coordinates['y']+1)):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x'],'y' : coordinates['y']+1})
                    #traversed.append({'x' : coordinates['x'],'y' : coordinates['y']+1})
                    queue.append(new_path)
                if( curr_cell.walls['W'] == False and {coordinates['x']-1,coordinates['y']} not in traversed and self.maze.is_valid_cell(coordinates['x']-1,coordinates['y'])):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x']-1,'y' : coordinates['y']})
                    #traversed.append({'x' : coordinates['x']-1,'y' : coordinates['y']})
                    queue.append(new_path)
