from weapon import *
from character import ZombieWolf, ZombieBear, ZombieGhost


class Room(object):

    def enter(self, hero):
        print "This room hasn't contructed yet please come back later"
        exit(1) 


class ZombieBearRoom(Room):

    def __init__(self):
        self.monster = ZombieBear()

    def enter(self, hero):
        if self.monster:
            print "You see a bear that has been effected by zombie virus"
            print "The bear is going to chew your head. Will you fight it?"
            print "You choose? (y/n)"
            answer = raw_input(">>")
            answer = answer.lower()
            if answer == "y":
                hero.fight(self.monster)
                self.monster.fight(hero)
                if not hero.is_alive():
                    return "death"
                if not self.monster.is_alive():
                    print "The bear is death under your hands. Great fight!!!"
                    self.monster = None
                return "zombie_bear"
            elif answer == "n":
                print "You run around and dodge the bear's attack but you can't dodge for long"
            else:
                print "You don't know what to do and the bear bites you"
                self.monster.fight(hero)
                if not hero.is_alive():
                    return "death"
                return "zombie_bear"
        print "You see a sign write 'High Level Armory ' in front of a door lead to a dark room"
        print "and a sign write 'Exit' in front of another door"
        print "You will go through which door?"
        print "1. High Level Armory"
        print "2. Exit"
	answer = raw_input(">>")
        if answer == "1":
            print "You go to Armory Room and hope finding strong weapon to fight the zombies"
            return "armory"
        elif answer == "2":
            print "You want to get out of here ASAP. You run to exit door"
            return "zombie_ghost"
        else:
            print "You run around and thinking"
            return "zombie_bear"


class ZombieWolfRoom(Room):
    
    def __init__(self):
        self.weapon = Sword()
        self.monster = ZombieWolf() 

    def enter(self, hero):
        if self.monster:
            print "You see a wolf that has been effected by zombie virus"
            print "The wolf is going to attack you. Will you fight it?"
            print "You choose?(y/n)"
            answer = raw_input(">>")
            answer = answer.lower()
            if answer == "y":
                hero.fight(self.monster)
                self.monster.fight(hero)
                if not hero.is_alive():
                    return "death"
                if not self.monster.is_alive():
                    print "The wolf is death under your hands. Great fight!!!"
                    self.monster = None
                return "zombie_wolf"
            elif answer == "n":
                print "You run around and dodge the wolf's attack but you can dodge for long"
            else:
                print "You don't know what to do and the wolf bites you"
                self.monster.fight(hero)
                if not hero.is_alive():
                    return "death"
                return "zombie_wolf"
        if self.weapon:
            print "You see an old %r at the corner of the room. You pick it?(y/n)" % self.weapon.name
            answer = raw_input(">>")
            answer = answer.lower()
            if answer == "y":
                hero.equip_weapon(self.weapon)
                self.weapon = None
            else:
                print "You choose to leave the %r there" % self.weapon.name
        print "You see one dark way ahead. Will you go through it?(y/n)"
        answer = raw_input(">>")
        answer = answer.lower()
        if answer == "y":
            print "You choose to go ahead. What a warrior, you afraid of nothing."
            return "zombie_ghost"
        else:
            print "You stay there and keep thinking. Great :)"
            return "zombie_wolf"


class ZombieGhostRoom(Room):

    def __init__(self):
        self.monster = ZombieGhost() 

    def enter(self, hero):
        print "You see the exit door in front of you."
        print "Unlucky, there is a HUGE zombie block the way. You have to defeat it to get through"
        while self.monster.is_alive():
            hero.fight(self.monster)
            self.monster.fight(hero)
            if not hero.is_alive():
                return "death"
        print "You have defeat the zombie ghost. Boss of all zombies in this maze."
        print "Every zombies in the maze now catch you up. You run through the exit door."
        print "You explode the gas around the door, many stones fall off and block the maze."
        return "exit"


class OpeningRoom(Room):

    def enter(self, hero):
        print """
        In 2020, the earth is in Zombie Apocalypse, you're a soldier have survived for a long time.
        In a midnight, when you searching for food, you face a huge group of zombies. In front of you
        is a maze that you have never gone through. You have only 2 options:
        1. Fight with those zombies
        2. Run into the maze
        What are you gonna do?
        """
        choice = raw_input(">>")
        if choice == "1":
            print """
            You stand still and prepare to fight with those zombies, one of them rush to you and bites
            your neck, you bleed to die.
            """
            hero.health -= hero.health
            return "death"
        elif choice == "2":
            print """
            One of those zombies suddenly rushes to you and bites, you dodge it and run into the maze,
            you have saved yourself.
            """
            return "cross_road"
        else:
            print """
            You confuse don't know what to do, those zombies approach you and tear you aparts. You die!
            """
            hero.health -= hero.health
            return "death"


class ArmoryRoom(Room):

    def __init__(self):
        self.weapon = FireGun()

    def expertise_container(self, hero):
        print "You see a big weapon container with a big steel chain around over your head"
        print "You have to use a weapon to break it. It may be a trap or it has powerful weapon inside."
        print "You choose:"
        print "1. Break it"
        print "2. Leave it"
        answer = raw_input(">>")
        if answer == "1" and hero.equiped_weapon:
            hero.deal_damage()
            print "You cut the chain and the container fall. In that container is a %r" % self.weapon.name
            print "That gun is huge and can defeat any enemy. Equip it?(yes/no)"
            answer = raw_input(">>")
            answer = answer.lower()
            if answer in ["yes", "y", "ok"]:
                hero.equip_weapon(self.weapon)
                self.weapon = None
            else:
                print "You choose to fight with your bare hands and left that %r there" % self.weapon.name
        elif not hero.equiped_weapon:
            print "You don't have anything to cut that chain off. Sorry"
        elif answer == "2":
            print "You afraid that could be a trap. What a coward!"
        else:
            print "You are thinking too much!!! The game is tired of you!!!"
        

    def enter(self, hero):
        if self.weapon:
            self.expertise_container(hero)
        print "There is two way ahead. One is very dark and one with the light. You choose"
        print "1. Dark way"
        print "2. Light way"
        answer = raw_input(">>")
        answer = answer.lower()
        if answer in ["1", "dark", "dark way"]:
            print "You choose to run into the dark way"
            return "zombie_ghost"
        elif answer in ["2", "light", "light way"]:
            print "You afraid of the dark and choose to go with the light way"
            return "zombie_wolf"
        else:
            print "You feel like you don't want to go anywhere. You tired"
            return "armory"

class CrossRoadRoom(Room):

    def __init__(self):
        self.weapon = Knife()

    def enter(self, hero):
        print "You walk into a doors room"
        if self.weapon:
            print "Under your toes is a %r" % self.weapon.name
            print "Will you pick it up?(yes/no)"
            answer = raw_input(">>")
            answer = answer.lower()
            if answer in ["yes", "y", "ok"]:
                hero.equip_weapon(self.weapon)
                self.weapon = None
            else:
                print "You choose to fight with your bare hands and left that %r there" % self.weapon.name
        print "There is 2 doors ahead. You have to choose one to go"
        print "1. Left door"
        print "2. Right door"
        print "Which door you choose?"
        answer = raw_input(">>")
        answer = answer.lower()
        if answer == "left":
            print "You open the left door and go ahead"
            return "zombie_wolf"
        elif answer == "right":
            print "You open the right door and go ahead"
            return "zombie_bear"
        else:
            print "You think too much. You have to choose now! The zombies will approach to you anytime"
            return "cross_road"

class ExitRoom(Room):

    def enter(self, hero):
        print "You have pass the maze and see a military base that have many people in it"
        print "Now you have a home to stay"
        print "Congratuation~~~"
        print "--------------------------------------------------------------------------"
        print "Hero stats:"
        print "Health: %r" % hero.health 
        print "Weapon: %r" % hero.equiped_weapon
        print "Damage: %r" % hero.deal_damage()

