class Light:
    def __init__(self, name):
        self.on = False
        self.name = name
        self.radio_button = None
        print(f"{self.name} has been initialised")

    def set_widget(self, radio_button):
        self.radio_button = radio_button

    def switch_on(self):
        self.on = True
        self.status()

    def switch_off(self):
        self.on = False
        self.status()

    def status(self):
        if self.radio_button is not None:
            self.radio_button.set(self.on)
        if self.on:
            print(self.name + " is on")
        else:
            print(self.name + " is off")
