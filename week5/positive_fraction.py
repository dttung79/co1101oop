class PositiveFraction:
    def __init__(self, numerator=0, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator
    
    def get_num(self):
        return self.__numerator
    
    def get_den(self):
        return self.__denominator
    
    def set_num(self, numerator):
        if numerator >= 0:
            self.__numerator = numerator
        else:
            print('Invalid numerator')
    
    def set_den(self, denominator):
        if denominator > 0:
            self.__denominator = denominator
        else:
            print('Invalid denominator')
    
    def print(self):
        print(self.__numerator, '/', self.__denominator, end='')
    
    def add(self, f):
        n = self.__numerator * f.get_den() + self.__denominator * f.get_num()
        d = self.__denominator * f.get_den()
        return PositiveFraction(n, d)
    
    def mul(self, f):
        n = self.__numerator * f.get_num()
        d = self.__denominator * f.get_den()
        return PositiveFraction(n, d)
    
    def div(self, f):
        if f.get_num() == 0:
            print('Cannot divide by zero')
            return None
        n = self.__numerator * f.get_den()
        d = self.__denominator * f.get_num()
        return PositiveFraction(n, d)

f1 = PositiveFraction(1, 2)
f2 = PositiveFraction(1, 3)

f3 = f1.add(f2)
f4 = f1.mul(f2)
f5 = f1.div(f2)

f3.print()
print()
f4.print()
print()
f5.print()