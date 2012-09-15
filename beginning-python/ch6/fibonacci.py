"""
This is a method to calculate fibonacci list from chapter 6
This is a good way to calculate fibonacci number
"""
fib = [0,1]
num = input('How many fibonacci numbers do you want?')
for n in range(num - 2):
    fib.append(fib[-2] + fib[-1])
#print fib

def fibonacci(num = input('How many fibonacci numbers do you want?')):
    """
    This method is to calculate the fibonacci list
    """
    fibs = [0,1]
    for n in range(num - 2):
       fibs.append(fibs[-2] + fibs[-1])
    return fibs

#use the fibonacci function
a = fibonacci()
print a
