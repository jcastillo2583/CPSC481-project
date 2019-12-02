import pygame
import Dungeon
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
    gen = Dungeon.Generator()
    gen.gen_level()
    gen.gen_tiles_level();
    gen.render(screen,  250, 0)
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        pygame.display.update()
    # MAZE LOGIC HERE

    #Exit Main loop & Stop game enprint("The final path: for bfs"+ str(path) + "\n")gine
    pygame.quit()






if __name__ == "__main__":
    main()
