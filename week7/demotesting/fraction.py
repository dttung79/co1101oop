class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
    
    @property
    def numerator(self):
        return self.__numerator
    
    @property
    def denominator(self):
        return self.__denominator
    
    def __str__(self):
        if self.numerator * self.denominator < 0:
            return f"-{abs(self.numerator)}/{abs(self.denominator)}"
        return f"{abs(self.numerator)}/{abs(self.denominator)}"
    
    def add(self, f):
        n = self.numerator * f.denominator + f.numerator * self.denominator
        d = self.denominator * f.denominator
        return Fraction(n, d)