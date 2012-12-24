__author__ = 'Lancewer'

#judge a num is larger smaller or equals 0
def foo(x):
    if x > 0:
        print 'The number %d is larger than 0' % x
    elif x < 0:
        print 'The number %d is smaller than 0' % x
    else:
        print 'The number %d is equals to 0' % x

foo(10)
foo(-1)
foo(0)
i = int(raw_input('Enter a number'))
foo(i)