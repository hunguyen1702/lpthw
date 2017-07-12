from random import randint


class Scence(object):

    def enter(self, hero):
        print "The director hasn't filmed this. Sorry :v"
        exit(1)
 

class Death(object):

    quips = [ 
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self, hero):
        print Death.quips[randint(0, len(self.quips) - 1)]
        exit(1)

