

class Player:

    def __init__(self, Maze, x ,y):
        self.maze_map = Maze.maze_map;
        self.x = x
        self.y = y

    def render(self, surface):
