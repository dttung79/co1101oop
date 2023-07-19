from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Shape name cannot be empty")
        self._name = value
    
    @property
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self.name} - area: {self.area:.2f}'

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        
        if self.__check_radius(radius):
            self._radius = radius
    
    def __check_radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius cannot be negative or zero")
        
        return True
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if self.__check_radius(value):
            self._radius = value

    @property
    def area(self):
        return 3.14 * self.radius ** 2
    
    def __str__(self):
        return super().__str__() + f', radius: {self.radius}'
    
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width cannot be negative or zero")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height cannot be negative or zero")
        self._height = value

    @property
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return super().__str__() + f', width: {self.width}, height: {self.height}'
    
class Triangle(Shape):
    def __init__(self, name, sidea, sideb, sidec):
        super().__init__(name)
        if not self.__check_sum(sidea, sideb, sidec):
            raise ValueError("Invalid triangle")
        self._sidea = sidea
        self._sideb = sideb
        self._sidec = sidec

    
    @property
    def sidea(self):
        return self._sidea
    
    @sidea.setter
    def sidea(self, value):
        if value <= 0:
            raise ValueError("Side A cannot be negative or zero")
        if self.__check_sum(value, self.sideb, self.sidec):
            raise ValueError("Invalid triangle")
        self._sidea = value
    
    @property
    def sideb(self):
        return self._sideb
    
    @sideb.setter
    def sideb(self, value):
        if value <= 0:
            raise ValueError("Side B cannot be negative or zero")
        if self.__check_sum(self.sidea, value, self.sidec):
            raise ValueError("Invalid triangle")
        self._sideb = value
    
    @property
    def sidec(self):
        return self._sidec
    
    @sidec.setter
    def sidec(self, value):
        if value <= 0:
            raise ValueError("Side C cannot be negative or zero")
        if self.__check_sum(self.sidea, self.sideb, value):
            raise ValueError("Invalid triangle")
        self._sidec = value
    
    def __check_sum(self, a, b, c):
        return a + b > c and b + c > a and c + a > b
    
    @property
    def area(self):
        p = (self.sidea + self.sideb + self.sidec) / 2
        return (p * (p - self.sidea) * (p - self.sideb) * (p - self.sidec)) ** 0.5
    
    def __str__(self):
        return super().__str__() + f', ({self.sidea}, {self.sideb}, {self.sidec})'
    
class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)

    @property
    def side(self):
        return self.width # or self.height
    
    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

class IsoTriangle(Triangle):
    def __init__(self, name, side, base):
        super().__init__(name, side, side, base)
    
    @property
    def side(self):
        return self.sidea # or sideb

    @side.setter
    def side(self, value):
        self.sidea = value # call setter of parent class, already validated
        self.sideb = value
    
    @property
    def base(self):
        return self.sidec
    
    @base.setter
    def base(self, value):
        self.sidec = value