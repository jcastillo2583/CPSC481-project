import pygame
import queue
from queue import PriorityQueue
from math import floor, ceil, sqrt, pow
from maze import Maze, Cell
class Minotaur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path_progress = 0
        self.target_path = []

    # def render(self, x=0 , y=0):
    #     #"""**SPAWN AT 0,0"""
    #
    #     self.x = x
    #     self.y = y
    #
    #     # l & w of rect = rec length - ( rect width * 2)
    #     """" If current is on ROW 0 --> rectangle vertical Padding = maze. ver_Padding + rect_Width  """
    #     if self.x == 0:
    #         y_start = ceil(self.maze.ver_padd + self.maze.rect_width)
    #     else:
    #         y_start = ceil(self.maze.ver_padd + self.y * self.maze.rect_length)
    #
    #     """If current is on COL 0 --> rect horizontal padding = maze.hori_padding + rect_Width"""
    #     if self.y == 0:
    #         x_start = ceil(self.maze.hori_padd + self.maze.rect_width)
    #     else:
    #         x_start = ceil(self.maze.hori_padd + self.x * self.maze.rect_length)
    #
    #     print("rendering the block at: ("+ str(x)+ ", "+str(y) + ")")
    #     print("x_start is: " + str(x_start))
    #     print("y_start is: " + str(y_start))
    #     pygame.draw.rect(self.surface, (255, 0, 255), ((x_start),(y_start), abs(self.maze.rect_length-(self.maze.rect_width*2)), abs(self.maze.rect_length-(self.maze.rect_width*2))))
    #     pygame.display.update()

    def walk_reset(self):
        self.path_progress=0;

    def walk(self):
        if len(self.target_path)>0 and self.path_progress< len(self.target_path):
            (self.x,self.y) = self.target_path[self.path_progress]
            print("new")
            print((self.x,self.y))
            self.path_progress += 1

    def distance_formula(self, begin, end):
            return sqrt(pow((end[1]-begin[1]),2) + pow((end[0]-begin[0]),2))

    def bfs(self, goal, graph):
        queue = []
        visited = []
        start = (self.x,self.y)
        queue.append(graph[start])

        while queue:
            path = queue.pop(0)

            node = path[-1]
            visited = visited + [node]
            if node == goal:
                print("we got it")
                print(path)
                self.target_path = path
                return path
            sorted_adjacent=[]
            for adjacent in graph[node]:
                sorted_adjacent.append((self.distance_formula(adjacent,goal), adjacent))

            sorted_adjacent = sorted(sorted_adjacent,key = lambda node: node[0])

            for adjacent in sorted_adjacent:
                if adjacent[1] not in visited:
                    new_path = list(path)
                    new_path.append(adjacent[1])
                    queue.append(new_path)

    def dfs(self, goal, graph):
        visited = []
        path = []
        fringe = PriorityQueue()
        start = (self.x,self.y)
        fringe.put((0,start,path,visited))
        while not fringe.empty():
            depth, current_node, path, visited  = fringe.get()
            if(current_node== goal):
                self.target_path = path + [current_node]    
            visited = visited + [current_node]
            child_nodes = graph[current_node]
            sorted_adjacent=[]
            for adjacent in graph[current_node]:
                sorted_adjacent.append((self.distance_formula(adjacent,goal), adjacent))

            sorted_adjacent = sorted(sorted_adjacent,key = lambda node: node[0])
            for value , node in sorted_adjacent:
                if node not in visited:
                    if node == goal:
                        return path +[node]
                    depth_of_node = len(path)
                    fringe.put((-depth_of_node, node, path+[node],visited))
        self.target_path = path
