import pygame
from Dungeon import Generator

class Player:

    def __init__(self, dungeon_array, x ,y):
        self.x = x
        self.y = y
        self.dungeon = dungeon_array

    def render(self, surface):


    def move(self, direction):
        # gets the key pressed when moving the Player
        direction = pygame.key.get_pressed()

        if direction[pygame.K_UP]:
            if self.dungeon[x-1][y] == 'floor':
                self.x -= 1
        if direction[pygame.K_DOWN]:
            if self.dungeon[x+1][y] == 'floor':
                self.x += 1
        if direction[pygame.K_RIGHT]:
            if self.dungeon[x][y+1] == 'floor':
                self.y += 1
        if direction[pygame.K_LEFT]:
            if self.dungeon[x][y-1] == 'floor':
                self.y -= 1
