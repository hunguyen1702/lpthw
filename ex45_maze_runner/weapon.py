class Weapon(object):

    def __init__(self):
        self.name = "Weapon"
        self.damage = 0
        self.stability = 0

    def decrease_stability(self):
        self.stability -= 1

    def is_broken(self):
        if self.stability < 1:
            print "%r is broken" % self.name
            return True
        return False

class Sword(Weapon):

    def __init__(self):
        self.name = "Sword"
        self.damage = 15
        self.stability = 3


class Knife(Weapon):

    def __init__(self):
        self.name = "Knife"
        self.damage = 5
        self.stability = 1


class FireGun(Weapon):

    def __init__(self):
        self.name = "FireGun"
        self.damage = 100 
        self.stability = 3

