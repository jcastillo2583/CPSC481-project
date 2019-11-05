import pygame
import queue
from queue import PriorityQueue
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
            y_start = floor(self.maze.ver_padd + self.maze.rect_width)
        else:
            y_start = floor(self.maze.ver_padd + self.y * self.maze.rect_length)

        """If current is on COL 0 --> rect horizontal padding = maze.hori_padding + rect_Width"""
        if self.y == 0:
            x_start = floor(self.maze.hori_padd + self.maze.rect_width)
        else:
            x_start = floor(self.maze.hori_padd + self.x * self.maze.rect_length)

        print("rendering the block at: ("+ str(x)+ ", "+str(y) + ")")
        print("x_start is: " + str(x_start))
        print("y_start is: " + str(y_start))
        pygame.draw.rect(self.surface, (255, 0, 255), (ceil(x_start), ceil(y_start), abs(self.maze.rect_length-(self.maze.rect_width*2)-20), abs(self.maze.rect_length-(self.maze.rect_width*2)-20)))
        pygame.display.update()



    def bfs(self, start, goal):
        queue = []
        traversed = []
        queue.append([{'x': start['x'], 'y': start['y']}])
        traversed.append({'x' : start['x'], 'y' : start['y']})
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
                if curr_cell.walls['N'] == False  and {'x':coordinates['x'],'y': coordinates['y']-1} not in traversed and self.maze.is_valid_cell(coordinates['x'],coordinates['y']-1):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x'],'y' : coordinates['y']-1})
                    #traversed.append({'x' : coordinates['x'],'y' : coordinates['y']-1})
                    queue.append(new_path)
                if( curr_cell.walls['E'] == False and {'x':coordinates['x']+1,'y':coordinates['y']} not in traversed and self.maze.is_valid_cell(coordinates['x']+1,coordinates['y'])):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x']+1,'y' : coordinates['y']})
                    #traversed.append({'x' : coordinates['x']+1,'y' : coordinates['y']})
                    queue.append(new_path)
                if( curr_cell.walls['S'] == False and {'x':coordinates['x'],'y':coordinates['y']+1} not in traversed and self.maze.is_valid_cell(coordinates['x'],coordinates['y']+1)):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x'],'y' : coordinates['y']+1})
                    #traversed.append({'x' : coordinates['x'],'y' : coordinates['y']+1})
                    queue.append(new_path)
                if( curr_cell.walls['W'] == False and {'x':coordinates['x']-1,'y': coordinates['y']} not in traversed and self.maze.is_valid_cell(coordinates['x']-1,coordinates['y'])):
                    new_path = list(path)
                    new_path.append({'x' : coordinates['x']-1,'y' : coordinates['y']})
                    #traversed.append({'x' : coordinates['x']-1,'y' : coordinates['y']})
                    queue.append(new_path)

    def dfs(self, start, goal):
        visited = []
        path = []
        fringe = PriorityQueue()
        fringe.put((0,start,path,visited))
        while not fringe.empty():
            depth, current_node, path, visited = fringe.get()

            if current_node  == goal:
                return path + [current_node]

            visited = visited + [(current_node['x'],current_node['y'])]

            curr_cell = self.maze.maze_map[current_node['x']][current_node['y']]
            #for eery childnode
            if curr_cell.walls['N'] == False  and (current_node['x'] , current_node['y']-1) not in visited and self.maze.is_valid_cell(current_node['x'],current_node['y']-1):
                node = {'x': current_node['x'],'y': current_node['y']-1}
                if node == goal:
                    return path +[node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path+[node],visited))
            if( curr_cell.walls['E'] == False and (current_node['x']+1,current_node['y']) not in visited and self.maze.is_valid_cell(current_node['x']+1,current_node['y'])):
                node = {'x': current_node['x']+1,'y': current_node['y']}
                if node == goal:
                    return path +[node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path+[node],visited))
            if( curr_cell.walls['S'] == False and (current_node['x'],current_node['y']+1) not in visited and self.maze.is_valid_cell(current_node['x'],current_node['y']+1)):
                node = {'x': current_node['x'],'y': current_node['y']+1}
                if node == goal:
                    return path +[node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path+[node],visited))
            if( curr_cell.walls['W'] == False and (current_node['x']-1,current_node['y']) not in visited and self.maze.is_valid_cell(current_node['x']-1,current_node['y'])):
                node = {'x': current_node['x']-1,'y': current_node['y']}
                if node == goal:
                    return path +[node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path+[node],visited))
        return visited

    def dfs_ver2(self, start,goal):
        graph = self.maze.get_graph()
        visited = []
        path = []
        fringe = PriorityQueue()
        fringe.put((0,start,path,visited))

        while not fringe.empty():
            depth, current_node, path, visited  = fringe.get()
            if(current_node== goal):
                return path +[current_node]

            visited = visited + [current_node]
            child_nodes = graph[current_node]
            for node in child_nodes:
                if node not in visited:
                    if node ==goal:
                        return path +[node]
                    depth_of_node = len(path)
                    fringe.put((-depth_of_node, node, path+[node],visited))
        return path
