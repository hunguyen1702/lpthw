my_name = 'Hung Nguyen'
my_age = 23 # not a lie
my_height = 165 # cm
my_weight = 52 # kg
my_eyes =  'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %ss eyes  and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the tea."  % my_teeth

# this line is tricky, try to get it exactly right
print "If iI add %d, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)
