#this one is like your script with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that *agrs is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just take one argument
def print_one(arg1):
    print "arg1: %r" % arg1


#this one take no argument
def print_none():
    print "I got nothing."


print_two("hung", "nv")
print_two_again("hung", "nv")
print_one("First!")
print_none()

