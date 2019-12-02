from __future__ import print_function
import PIL
from math import ceil , floor
import pygame
import random
import datetime as dt
from Minotaur import Minotaur
from Player import Player

CHARACTER_TILES = {'stone': ' ',

                   'floor': '.',

                   'wall': '#'}

class Generator():

    def __init__(self, width=64, height=64, max_rooms=15, min_room_xy=5,

                 max_room_xy=10, rooms_overlap=False, random_connections=1,

                 random_spurs=3, tiles=CHARACTER_TILES):

        self.width = width
        self.height = height
        self.max_rooms = max_rooms
        self.min_room_xy = min_room_xy
        self.max_room_xy = max_room_xy
        self.rooms_overlap = rooms_overlap
        self.random_connections = random_connections
        self.random_spurs = random_spurs
        self.tiles = CHARACTER_TILES
        self.level = []
        self.room_list = []
        self.corridor_list = []
        self.tiles_level = []


        self.update_clock = -1
        self.walk_clock = -1
        self.enemy_list = []
        self.goal = (-1,-1)
        self.key = (-1,-1)
        self.has_key = False;
        self.player = Player(self.level,0,0)



    def gen_room(self):
        x, y, w, h = 0, 0, 0, 0
        w = random.randint(self.min_room_xy, self.max_room_xy)
        h = random.randint(self.min_room_xy, self.max_room_xy)
        x = random.randint(1, (self.width - w - 1))
        y = random.randint(1, (self.height - h - 1))
        return [x, y, w, h]



    def room_overlapping(self, room, room_list):
        x = room[0]
        y = room[1]
        w = room[2]
        h = room[3]
        for current_room in room_list:
            # The rectangles don't overlap if
            # one rectangle's minimum in some dimension
            # is greater than the other's maximum in
            # that dimension.
            if (x < (current_room[0] + current_room[2]) and

                current_room[0] < (x + w) and

                y < (current_room[1] + current_room[3]) and

                current_room[1] < (y + h)):
                return True
        return False

    def corridor_between_points(self, x1, y1, x2, y2, join_type='either'):
        if x1 == x2 and y1 == y2 or x1 == x2 or y1 == y2:
            return [(x1, y1), (x2, y2)]
        else:
            # 2 Corridors
            # NOTE: Never randomly choose a join that will go out of bounds
            # when the walls are added.
            join = None

            if join_type is 'either' and set([0, 1]).intersection(set([x1, x2, y1, y2])):
                join = 'bottom'
            elif join_type is 'either' and set([self.width - 1,self.width - 2]).intersection(set([x1, x2])) or set([self.height - 1, self.height - 2]).intersection(set([y1, y2])):
                join = 'top'
            elif join_type is 'either':
                join = random.choice(['top', 'bottom'])
            else:
                join = join_type
            if join is 'top':
                return [(x1, y1), (x1, y2), (x2, y2)]
            elif join is 'bottom':
                return [(x1, y1), (x2, y1), (x2, y2)]

    def play_game(self):
        direction = pygame.key.get_pressed()
        self.player.move(direction)

    def join_rooms(self, room_1, room_2, join_type='either'):
        sorted_room = [room_1, room_2]
        sorted_room.sort(key=lambda x_y: x_y[0])

        x1 = sorted_room[0][0]
        y1 = sorted_room[0][1]
        w1 = sorted_room[0][2]
        h1 = sorted_room[0][3]
        x1_2 = x1 + w1 - 1
        y1_2 = y1 + h1 - 1

        x2 = sorted_room[1][0]
        y2 = sorted_room[1][1]
        w2 = sorted_room[1][2]
        h2 = sorted_room[1][3]
        x2_2 = x2 + w2 - 1
        y2_2 = y2 + h2 - 1
        if x1 < (x2 + w2) and x2 < (x1 + w1):
            jx1 = random.randint(x2, x1_2)
            jx2 = jx1
            tmp_y = [y1, y2, y1_2, y2_2]
            tmp_y.sort()
            jy1 = tmp_y[1] + 1
            jy2 = tmp_y[2] - 1
            corridors = self.corridor_between_points(jx1, jy1, jx2, jy2)
            self.corridor_list.append(corridors)
        # overlapping on y
        elif y1 < (y2 + h2) and y2 < (y1 + h1):
            if y2 > y1:
                jy1 = random.randint(y2, y1_2)
                jy2 = jy1
            else:
                jy1 = random.randint(y1, y2_2)
                jy2 = jy1
            tmp_x = [x1, x2, x1_2, x2_2]
            tmp_x.sort()
            jx1 = tmp_x[1] + 1
            jx2 = tmp_x[2] - 1
            corridors = self.corridor_between_points(jx1, jy1, jx2, jy2)
            self.corridor_list.append(corridors)
        # no overlap
        else:
            join = None
            if join_type is 'either':
                join = random.choice(['top', 'bottom'])
            else:
                join = join_type
            if join is 'top':
                if y2 > y1:
                    jx1 = x1_2 + 1
                    jy1 = random.randint(y1, y1_2)
                    jx2 = random.randint(x2, x2_2)
                    jy2 = y2 - 1
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'bottom')
                    self.corridor_list.append(corridors)
                else:
                    jx1 = random.randint(x1, x1_2)
                    jy1 = y1 - 1
                    jx2 = x2 - 1
                    jy2 = random.randint(y2, y2_2)
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'top')
                    self.corridor_list.append(corridors)

            elif join is 'bottom':
                if y2 > y1:
                    jx1 = random.randint(x1, x1_2)
                    jy1 = y1_2 + 1
                    jx2 = x2 - 1
                    jy2 = random.randint(y2, y2_2)
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'top')
                    self.corridor_list.append(corridors)
                else:
                    jx1 = x1_2 + 1
                    jy1 = random.randint(y1, y1_2)
                    jx2 = random.randint(x2, x2_2)
                    jy2 = y2_2 + 1
                    corridors = self.corridor_between_points(
                        jx1, jy1, jx2, jy2, 'bottom')
                    self.corridor_list.append(corridors)

    def gen_level(self):
        # build an empty dungeon, blank the room and corridor lists
        for i in range(self.height):
            self.level.append(['stone'] * self.width)
        self.room_list = []
        self.corridor_list = []
        max_iters = self.max_rooms * 5
        for a in range(max_iters):
            tmp_room = self.gen_room()
            if self.rooms_overlap or not self.room_list:
                self.room_list.append(tmp_room)
            else:
                tmp_room = self.gen_room()
                tmp_room_list = self.room_list[:]
                if self.room_overlapping(tmp_room, tmp_room_list) is False:
                    self.room_list.append(tmp_room)
            if len(self.room_list) >= self.max_rooms:
                break
        # connect the rooms
        for a in range(len(self.room_list) - 1):
            self.join_rooms(self.room_list[a], self.room_list[a + 1])
        # do the random joins
        for a in range(self.random_connections):
            room_1 = self.room_list[random.randint(0, len(self.room_list) - 1)]
            room_2 = self.room_list[random.randint(0, len(self.room_list) - 1)]
            self.join_rooms(room_1, room_2)
        # do the spurs
        for a in range(self.random_spurs):
            room_1 = [random.randint(2, self.width - 2), random.randint(
                     2, self.height - 2), 1, 1]
            room_2 = self.room_list[random.randint(0, len(self.room_list) - 1)]
            self.join_rooms(room_1, room_2)
        # fill the map
        # paint rooms
        for room_num, room in enumerate(self.room_list):
            for b in range(room[2]):
                for c in range(room[3]):
                    self.level[room[1] + c][room[0] + b] = 'floor'
        # paint corridors
        for corridor in self.corridor_list:
            x1, y1 = corridor[0]
            x2, y2 = corridor[1]
            for width in range(abs(x1 - x2) + 1):
                for height in range(abs(y1 - y2) + 1):
                    self.level[min(y1, y2) + height][
                        min(x1, x2) + width] = 'floor'
            if len(corridor) == 3:
                x3, y3 = corridor[2]
                for width in range(abs(x2 - x3) + 1):
                    for height in range(abs(y2 - y3) + 1):
                        self.level[min(y2, y3) + height][
                            min(x2, x3) + width] = 'floor'

        for row in range(1, self.height - 1):
            for col in range(1, self.width - 1):
                if self.level[row][col] == 'floor':
                    if self.level[row - 1][col - 1] == 'stone':
                        self.level[row - 1][col - 1] = 'wall'
                    if self.level[row - 1][col] == 'stone':
                        self.level[row - 1][col] = 'wall'
                    if self.level[row - 1][col + 1] == 'stone':
                        self.level[row - 1][col + 1] = 'wall'
                    if self.level[row][col - 1] == 'stone':
                        self.level[row][col - 1] = 'wall'
                    if self.level[row][col + 1] == 'stone':
                        self.level[row][col + 1] = 'wall'
                    if self.level[row + 1][col - 1] == 'stone':
                        self.level[row + 1][col - 1] = 'wall'
                    if self.level[row + 1][col] == 'stone':
                        self.level[row + 1][col] = 'wall'
                    if self.level[row + 1][col + 1] == 'stone':
                        self.level[row + 1][col + 1] = 'wall'


        r = random.randint(0, self.height- 1)
        c = random.randint(0, self.width- 1)
        while (self.level[r][c] != 'floor'):
            r = random.randint(0, self.height - 1)
            c = random.randint(0, self.width - 1)
        self.goal = (r,c)
        r = random.randint(0, self.height- 1)
        c = random.randint(0, self.width- 1)
        while (self.level[r][c] != 'floor' and (r,c) != self.goal):
            r = random.randint(0, self.height - 1)
            c = random.randint(0, self.width - 1)
        self.key = (r,c)
        r = random.randint(0, self.height- 1)
        c = random.randint(0, self.width - 1)
        while (self.level[r][c] != 'floor' and (r,c) != self.goal and (r,c) != self.key):
            r = random.randint(0, self.height - 1)
            c = random.randint(0, self.width - 1)
        print(self.level[r][c])
        (self.player.x, self.player.y) = (r, c)
        self.player.dungeon = self.level




    def gen_enemies(self, num = 1):
        for i in range(0, num):
            r = random.randint(0, self.height - 1)
            c = random.randint(0, self.width - 1)
            while (self.level[r][c] != 'floor'):
                r = random.randint(0, self.height - 1)
                c = random.randint(0, self.width - 1)
            new_enemy = Minotaur(r,c)
            self.enemy_list.append(new_enemy)


    def gen_tiles_level(self):
        for row_num, row in enumerate(self.level):
            tmp_tiles = []
            for col_num, col in enumerate(row):
                if col == 'stone':
                    tmp_tiles.append(self.tiles['stone'])
                if col == 'floor':
                    tmp_tiles.append(self.tiles['floor'])
                if col == 'wall':
                    tmp_tiles.append(self.tiles['wall'])
            self.tiles_level.append(''.join(tmp_tiles))
        print('Room List: ', self.room_list)
        print('\nCorridor List: ', self.corridor_list)
        [print(row) for row in self.tiles_level]

    def get_graph(self):
        graph = {}
        for x in range(0,self.width-1):
            for y in range(0,self.height-1):
                graph.update({(x,y) : []})
                if( self.is_valid_cell(x-1,y) and self.level[x-1][y]=='floor'):
                    graph[(x,y)].append((x-1,y))
                if(  self.is_valid_cell(x,y+1) and self.level[x][y+1]=='floor'):
                    graph[(x,y)].append((x,y+1))
                if( self.is_valid_cell(x+1,y)and  self.level[x+1][y] == 'floor'):
                    graph[(x,y)].append((x+1,y))
                if(self.is_valid_cell(x,y-1)and self.level[x][y-1] == 'floor'):
                    graph[(x,y)].append((x,y-1))
        return graph

    def is_valid_cell(self,x,y):
        if( x >= 0 and x < self.height and y >= 0 and y < self.width):
            return True
        else:
            return False

    def update_ai(self):
        for enemy in self.enemy_list:
            enemy.bfs((self.player.x,self.player.y),self.get_graph())
            enemy.walk_reset()


    def ai_walk(self, walk_interval,update_interval):
        if(self.update_clock == -1):
            self.update_clock = dt.datetime.now()
            self.walk_clock = dt.datetime.now()
        if update_interval < (dt.datetime.now() - self.update_clock).total_seconds():
            self.update_ai()
            self.update_clock = dt.datetime.now()

        if walk_interval < (dt.datetime.now() - self.walk_clock).total_seconds():
            for enemy in self.enemy_list:
                enemy.walk()
                print("Walking")
            self.walk_clock = dt.datetime.now()



    def check_state(self):
        for enemy in self.enemy_list:
            if (enemy.x,enemy.y) == (self.player.x,self.player.y):
                return "lose"
        if (self.player.x,self.player.y) == self.goal and self.has_key:
            return "win"
        if (self.player.x,self.player.y) == self.key:
              self.has_key = True

    def render(self, surface, hori_padd, ver_padd):
        square_length = abs(floor((surface.get_height()-ver_padd*2)/self.height))

        #```Resize the Images to the appropriate size for the size of the screen```
        #All these images are different resolutions so we need to figure out the
        #scaling for each one individually.
        stone = 'resources/cobble.jpeg'
        dirt = 'resources/dirt.jpeg'
        lava ='resources/lava.jpg'

    #    ``` After We scaled all the images put them into pygame image objects? ```
        game_stone = pygame.image.load(stone)
        game_stone = pygame.transform.scale(game_stone, (square_length, square_length))
        game_dirt = pygame.image.load(dirt)
        game_dirt= pygame.transform.scale(game_dirt, (square_length, square_length))
        game_lava = pygame.image.load(lava)
        game_lava= pygame.transform.scale(game_lava, (square_length, square_length))

#
#        ``` Set the initial rendering position ```
        row_pixel = ver_padd
        col_pixel = hori_padd
        for row in self.tiles_level:
            for tile in row :
                if tile == '#':
                    surface.blit(game_stone,(col_pixel,row_pixel))
                elif tile == '.':
                    surface.blit(game_dirt,(col_pixel,row_pixel))
                elif tile == ' ':
                    surface.blit(game_lava,(col_pixel,row_pixel))
                else:
                    print("Something went wrong")
                    exit(0)
                col_pixel = col_pixel + square_length
            col_pixel = hori_padd
            row_pixel = row_pixel + square_length

        # Pick a god and pray
        """ Then we gotta render the Minotaur, player, k """
        if self.has_key:
            down_stairs= pygame.image.load('resources/stairs.png')
            down_stairs= pygame.transform.scale(down_stairs, (square_length, square_length))
            surface.blit(down_stairs, (hori_padd + self.goal[1]*square_length, ver_padd + self.goal[0]*square_length))
        else:
            key= pygame.image.load('resources/key.png')
            key= pygame.transform.scale(key, (square_length, square_length))
            surface.blit(key, (hori_padd + self.key[1]*square_length, ver_padd + self.key[0]*square_length))
            closed_door= pygame.image.load('resources/closed.png')
            closed_door= pygame.transform.scale(closed_door, (square_length, square_length))
            surface.blit(closed_door, (hori_padd + self.goal[1]*square_length, ver_padd + self.goal[0]*square_length))
        game_enemy = pygame.image.load('resources/enemy.png')
        game_enemy = pygame.transform.scale(game_enemy, (square_length, square_length))
        for enemy in self.enemy_list:
            surface.blit(game_enemy, (hori_padd + enemy.y*square_length, ver_padd + enemy.x*square_length))
        self.player.render(surface,hori_padd,ver_padd,square_length)
