__author__ = 'Lancewer'

# Get a string from input, then print it out
str = raw_input('Enter a String: ')
print str

#Get a number from user, then print it out
numStr = raw_input('Enter a Number:')
num =  int(numStr)
print 'You input %d and type is %s' % (num, num.__class__)