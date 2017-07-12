from engine import Engine
from maze import Maze
from character import Runner


try:
    maze_map = Maze('opening')
    hero = Runner()
    game_engine = Engine(maze_map, hero)
    game_engine.play()
except EOFError, e:
    print "You quit the game, there is no saved game for you"
except KeyboardInterrupt, e:
    print "You shut the game down by a violent way."
 
