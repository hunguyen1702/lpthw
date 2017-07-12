class Character(object):
    """Character in maze"""

    def __init__(self):
        """Init character's health, damage, name"""
        self.health = 0
        self.damage = 0
        self.name = "NoName"

    def deal_damage(self):
        """return damage dealt by character"""
        return self.damage

    def fight(self, enemy):
        """Attack enemy"""
        enemy.health -= self.deal_damage()
        print "%r deal %r to %r. (%r: %r health, %r: %r health)" % (self.name, self.deal_damage(), enemy.name,
                                                                    self.name, self.health, enemy.name, enemy.health)

    def is_alive(self):
        """Check if character's health is greater than 0"""
        if self.health < 1:
            print "%r die" % self.name
            return False
        return True


class Runner(Character):

    def __init__(self):
        self.health = 100
        self.damage = 10
        self.equiped_weapon = None
        self.name = "You"

    def deal_damage(self):
        """Override method to add damage of hero weapon, and decrease weapon stability by 1"""
        if self.equiped_weapon is not None:
            self.equiped_weapon.decrease_stability()
            return self.damage + self.equiped_weapon.damage
        return self.damage

    def fight(self, enemy):
        """Override method to fight and check if weapon broke or not"""
        super(Runner, self).fight(enemy)
        if self.equiped_weapon and self.equiped_weapon.is_broken():
            self.equiped_weapon = None    

    def equip_weapon(self, weapon):
        """Hero pickup a weapon and discard the weapon in his hand"""
        print "You have picked up a(n) %r" % weapon.name
        if self.equiped_weapon:
            print "You have discarded your %r" % self.equiped_weapon.name
        self.equiped_weapon = weapon


class ZombieBear(Character):

    def __init__(self):
        self.health = 75 
        self.damage = 20
        self.name = "Zombie Bear"

class ZombieWolf(Character):

    def __init__(self):
        self.health = 50
        self.damage = 30
        self.name = "Zombie Wolf"


class ZombieGhost(Character):

    def __init__(self):
        self.health = 200
        self.damage = 35
        self.name = "Zombie Ghost"

