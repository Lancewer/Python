__author__ = 'Lancewer'
my_name = 'Zed A. Shaw'
my_age = 35  #not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eye = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print  "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eye, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky , try to get it exactly right
print "If I add %d, %d, and  %d I get %d." % (my_age, my_weight, my_height, my_age + my_weight + my_height)

#Additional exercises
print "This line contains %r and %r" % ("Hello", 4)