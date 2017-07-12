from room import *
from scene import Death


class Maze(object):
    """A maze with a dict of {name: room} pairs pre-defined. When
       the game is loaded, all rooms have created"""

    rooms = {
        "zombie_bear": ZombieBearRoom(),
        "zombie_wolf": ZombieWolfRoom(),
        "zombie_ghost": ZombieGhostRoom(),
        "opening": OpeningRoom(),
        "armory": ArmoryRoom(),
        "cross_road": CrossRoadRoom(),
        "exit": ExitRoom(),
        "death": Death() 
    }

    def __init__(self, start_room):
        """Init a maze map with a start room"""
        self.start_room = start_room

    def next_room(self, room_name):
        """Get next room instance by room's name key"""
        return Maze.rooms.get(room_name)

    def start_maze(self):
        """Get next room instance after the start room"""
        return self.next_room(self.start_room)

