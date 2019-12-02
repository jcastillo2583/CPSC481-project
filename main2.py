import pygame
import Dungeon
import argparse
def main():
    # parser = argparse.ArgumentParser(description='CPSC 481 Project')
    # parser.add_argument('-s', '--size', type=int ,default = 64, help = "Usage:-f <filename>.csv\nThis will write the results to the file specified.")
    # parser.add_argument('-d', '--difficulty', type=str,default = 'normal', help = "Usage:-f <filename>.csv\nThis will write the results to the file specified.")
    # parser.add_argument('-n', '--number', type =int, default = 1, help= "The number of adversary AI you want to spawn")
    # parser.add_argument('-r', '--rooms', type =int, default = 4, help= "The number of \'rooms\' you want to spawn")
    pygame.init()
    # COLORS
    black = (0, 0, 0)
    white = (255, 255, 255)

    # WINDOW
    screen = pygame.display.set_mode((0,0))
    screen = pygame.display.set_mode((screen.get_height()-160,screen.get_height()-160))
    pygame.display.set_caption("Minotaur Maze")

    #GAME LOOP: Plays game until user exit
    gameLoop = True

    # MAN PROGRAM LOOP
    dungeon = Dungeon.Generator(40, 40, 5, 5 ,15)
    dungeon.gen_level()
    dungeon.gen_tiles_level()
    dungeon.gen_enemies(1)
    dungeon.update_ai()
    levels_completed =0
    #pygame.key.set_repeat(0,1500)
    #dungeon.update_ai()
    #dungeon.play_game()

    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            if event.type == pygame.KEYDOWN:
                dungeon.play_game()
        dungeon.ai_walk(0.5,10)
        dungeon.render(screen,  0, 10)
        state = dungeon.check_state()
        if(state == "lose"):
            gameLoop = False
            print("You completed "+ to_string(levels_completed)+ " levels!")
        elif(state == "win"):
            play_again = input("On to the next level? Y/n:")
            if(play_again == "Y"):
                dungeon = Dungeon.Generator(40, 40, 5, 3,4)
                dungeon.gen_level()
                dungeon.gen_tiles_level()
                dungeon.gen_enemies(2)
                dungeon.update_ai()
                dungeon.render(screen,  250, 10)
            else:
                gameLoop = False
                #print("You completed "+ to_string(levels_completed)+ " levels!")


        pygame.display.update()
    # # MAZE LOGIC HERE
    #
    # #Exit Main loop & Stop game enprint("The final path: for bfs"+ str(path) + "\n")gine
    # pygame.quit()
    #
    #
    #
    #
    #

if __name__ == "__main__":
    main()
