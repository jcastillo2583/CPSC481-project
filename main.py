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
    maze = Maze(screen, 30,30)
    maze.make_maze()
    maze.render()
    mino = Minotaur(screen,maze,0,0)
    mino.render()
    graph = { (1,2): (1,2,3)}
    graph = maze.get_graph()
    #print(graph)
    ###CHANGE THIS TO CHANG THE GOALS
            #BEGIN              #END
    #path = mino.bfs({'x':0 , 'y':0}, {'x':1 , 'y': 3})
    pathdfs = mino.dfs_ver2((0,0), (4,4))
    #structs = maze.generate_structures()
    #maze.connect_strucutres(structs)
    maze.render()
    for node in pathdfs:
        mino.render(node[0],node[1])
        pygame.time.delay(100)
    print("The final path: for dfs"+ str(pathdfs) + "\n")
    #print("The final path: for bfs"+ str(path) + "\n")
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        pygame.display.update()
    # MAZE LOGIC HERE

    #Exit Main loop & Stop game enprint("The final path: for bfs"+ str(path) + "\n")gine
    pygame.quit()
    print(str(maze))






if __name__ == "__main__":
    main()
