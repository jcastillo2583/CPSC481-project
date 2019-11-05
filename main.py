import pygame
from Minotaur import Minotaur
from maze import Maze, Cell
def main():
    pygame.init()
    # COLORS
    black = (0, 0, 0)
    white = (255, 255, 255)

    # WINDOW
    screen = pygame.display.set_mode((0,0))
    screen = pygame.display.set_mode((screen.get_width()-160,screen.get_height()-160))
    pygame.display.set_caption("Minotaur Maze")

    #GAME LOOP: Plays game until user exit
    gameLoop = True

    # MAN PROGRAM LOOP
    print("The Width is: " + str(screen.get_width()))
    print("The Height is: " + str(screen.get_height()))
    maze = Maze(screen, 10,10)
    maze.make_maze()
    maze.render()
    mino = Minotaur(screen,maze,0,0)
    mino.render()

    ###CHANGE THIS TO CHANG THE GOALS
            #BEGIN              #END
    mino.bfs({'x':0 , 'y':0}, {'x':1 , 'y':2})
    #structs = maze.generate_structures()
    #maze.connect_strucutres(structs)

    maze.render()
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        pygame.display.update()
    # MAZE LOGIC HERE

    #Exit Main loop & Stop game engine
    pygame.quit()
    print(str(maze))






if __name__ == "__main__":
    main()
