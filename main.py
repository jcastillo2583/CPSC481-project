import pygame
from maze import Maze, Cell
def main():

    pygame.init()
    # COLORS
    black = (0, 0, 0)
    white = (255, 255, 255)

    # WINDOW
    windowSize = (800, 500)
    screen = pygame.display.set_mode(windowSize)
    pygame.display.set_caption("Minotaur Maze")

    #GAME LOOP: Plays game until user exit
    gameLoop = True

    # MAN PROGRAM LOOP
    maze = Maze(10,10)
    maze.make_maze()
    maze.render(screen,800,500,10)
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
