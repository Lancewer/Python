"""
This is a method to calculate fibonacci list from chapter 6
This is a good way to calculate fibonacci number
"""
fibs = [0,1]
num = input('How many fibonacci numbers do you want?')
for n in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1])
print fibs
