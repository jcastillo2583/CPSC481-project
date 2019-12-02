
import pygame

class Player:
    def __init__(self, dungeon_array, x ,y):
        self.x = x
        self.y = y
        self.dungeon = dungeon_array
        self.orientation = 'NEUTRAL'

    def render(self, surface, hori_padd, ver_padd, size):
        if self.orientation == 'NEUTRAL':
            neutral= pygame.image.load('resources/player_neutral.png')
            neutral = pygame.transform.scale(neutral, (size, size))
            surface.blit(neutral, (hori_padd + self.y*size, ver_padd + self.x*size))
        if self.orientation == 'UP':
            up = pygame.image.load('resources/player_up.png')
            up = pygame.transform.scale(up, (size, size))
            surface.blit(up, (hori_padd + self.y*size, ver_padd + self.x*size))
        if self.orientation == 'DOWN':
            down = pygame.image.load('resources/player_down.png')
            down = pygame.transform.scale(down, (size, size))
            surface.blit(down, (hori_padd + self.y*size, ver_padd + self.x*size))
        if self.orientation == 'LEFT':
            left = pygame.image.load('resources/player_left.png')
            left = pygame.transform.scale(left, (size, size))
            surface.blit(left, (hori_padd + self.y*size, ver_padd + self.x*size))
        if self.orientation == 'RIGHT':
            right = pygame.image.load('resources/player_right.png')
            right = pygame.transform.scale(right, (size, size))
            surface.blit(right, (hori_padd + self.y*size, ver_padd + self.x*size))



    def move(self, direction):
        # gets the key pressed when moving the Player


        if direction[pygame.K_UP]:
            if self.dungeon[self.x-1][self.y] == 'floor':
                self.x -= 1
                self.orientation = 'UP'
        if direction[pygame.K_DOWN]:
            if self.dungeon[self.x+1][self.y] == 'floor':
                self.x += 1
                self.orientation = 'DOWN'
        if direction[pygame.K_RIGHT]:
            if self.dungeon[self.x][self.y+1] == 'floor':
                self.y += 1
                self.orientation = 'RIGHT'
        if direction[pygame.K_LEFT]:
            if self.dungeon[self.x][self.y-1] == 'floor':
                self.y -= 1
                self.orientation = 'LEFT'
        print("Player moved to")
        print((self.x,self.y))
