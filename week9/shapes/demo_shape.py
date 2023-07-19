from shape import Shape, Circle, Rectangle, Triangle, Square, IsoTriangle
from menu import Menu

# Create a class DemoShape (inherite from Menu)
# Provide following options:
# 1. Add a circle
# 2. Add a rectangle
# 3. Add a triangle
# 4. Add a square
# 5. Add an isosceles triangle
# 6. Display all shapes

class DemoShape(Menu):
    def __init__(self):
        self.__shapes = []
    
    def print_menu(self):
        print("1. Add a circle")
        print("2. Add a rectangle")
        print("3. Add a triangle")
        print("4. Add a square")
        print("5. Add an isosceles triangle")
        print("6. Display all shapes")
        print("0. Exit")
    
    def __add_circle(self):
        name = input("Enter name: ")
        radius = float(input("Enter radius: "))
        try:
            circle = Circle(name, radius)
            self.__shapes.append(circle)
        except ValueError as e:
            print(e, 'Cannot add circle')