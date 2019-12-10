# CPSC481-project
# How to run the Minotaur AI Maze

1.) If you do not have pygame and Pillow installed already, use the commands
       pip3 install pygame
       pip3 install Pillow  
       
2.) Download the zip file that has all of the necessary files.   

3.) Select the main2.py to run the program


# FILE DESCRIPTIONS
Dungeon.py
       - This file generates the game's maze/dungeon. The class Generator() includes numerous features of the maze such as the maze's width, height, tiles, and the rooms within the maze/dungeon. Generator() includes several functions that essentially updates the dungeon when a move from either the player or AI has occurred. Furthermore, these functions generate the 4 rooms within the dungeon, generate corridors/hallways that connect rooms, generate the Minotaur enemies, and renders the images used for the Minotaur and Player characters as well as the surrounding walls and cells for the maze/dungeon. 
       
main2.py
       - This is the main driver for the program. The main GUI window is implemented here along with the game loop. A dungeon is first created before the program enters the game loop.
       
maze.py
       - This file generates the overall maze in the dungeon. This file also generates the cells and its surrounding walls within the maze. Each cell may be surrounded by north, east, south, or west walls. We utilized Christian Hill's 2017 depth-first algorithm to help us generate the maze. Essentially, the program starts at a specific coordinate and creates a random structure for the maze, finding cell neighbors and establishing where to knock down the wall to create a path.
       
Minotaur.py
       - This file generates the Minotaur character and its behavior. The functions included in the file are the critical algorithms and formulas that drive the Minotaur. Such algorithms and formulas include the distance formula, best first search, and depth first search algorithms. 
       
Player.py
       - This file generates the player character. The function render() sets different images/views of the player for every direction it is facing. The function move() receives the user's desired direction and utilizes key listeners to move in the specified direction. Additionally, the player's position updates as the player selects the different directions.
