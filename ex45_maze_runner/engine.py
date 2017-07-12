from maze import Maze


class Engine(object):
    """The engine of the game, make a hero character and maze map work"""
    def __init__(self, maze_map, hero):
        """Init an game engine with a new maze map and new hero character"""
        self.maze_map = maze_map
        self.hero = hero

    def play(self):
        """play the game from the start room until the hero reaches the exit room"""
        current_room = self.maze_map.start_maze()
        last_room = self.maze_map.next_room('exit')

        while current_room is not last_room:
            next_room_name = current_room.enter(self.hero)
            current_room = self.maze_map.next_room(next_room_name)

        last_room.enter()

