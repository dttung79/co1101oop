from shape import Shape, Circle, Rectangle, Triangle, Square, IsoTriangle


obj1 = Shape("Shape 1")
obj2 = Circle("Circle 1", 10)
obj3 = Rectangle("Rectangle 1", 10, 20)
obj4 = Triangle("Triangle 1", 10, 20, 14)
obj5 = Square("Square 1", 10)
obj6 = IsoTriangle("IsoTriangle 1", 10, 5)

shapes = [obj1, obj2, obj3, obj4, obj5, obj6]

for s in shapes:
    print(s.area)