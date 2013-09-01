__author__ = 'lawrence'
class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise

calculator = MuffledCalculator()
calculator.calc('10/2')
#calculator.calc('10/0') #This line will cause an exception
calculator.muffled = True
calculator.calc('10/0')

calc2 = MuffledCalculator()
print calc2.muffled
print calculator.muffled