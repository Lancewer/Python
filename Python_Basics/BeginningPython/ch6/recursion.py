'''6.6 recursion'''
__author__ = 'Lancewer'

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print factorial(20)
