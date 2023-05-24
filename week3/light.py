class Light:
    # __init__ is a special method that is called when an object is created 
    # __init__ is a constructor in OOP terms
    def __init__(self):
        self.name = "Light"
        self.type = "Brightness"
        self.level = 200
        self.status = True
    # turn on the light
    def turn_on(self):
        self.status = True
        print("Light is on")
    # turn off the light
    def turn_off(self):
        self.status = False
        print("Light is off")
    # increase the brightness
    def increase(self):
        self.level += 1
        print(f"Light brightness is increase to {self.level}")
    # decrease the brightness
    def decrease(self):
        self.level -= 1
        print(f"Light brightness is decrease to {self.level}")