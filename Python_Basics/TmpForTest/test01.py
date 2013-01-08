import sys
import datetime

print sys.path

print sys.argv

class Hi():
    def sayHi(self):
        print "Hello from Hi.sayHi"

if __name__ == '__main__':
    print "this module is run by itself"
else:
    print "This module is run by others"

print __name__