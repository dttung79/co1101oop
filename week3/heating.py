class Heating:
    # __init__ is a special method that is called when an object is created 
    # __init__ is a constructor in OOP terms
    def __init__(self):
        self.name = "Heating"
        self.type = "Temperature"
        self.level = 20
        self.status = True
    # turn on the light
    def turn_on(self):
        self.status = True
        print("Heating is on")
    # turn off the light
    def turn_off(self):
        self.status = False
        print("Heating is off")
    # increase the brightness
    def increase(self):
        self.level += 1
        print(f"Temperature is increased to {self.level}")
    # decrease the brightness
    def decrease(self):
        self.level -= 1
        print(f"Temperature is decreased to {self.level}")