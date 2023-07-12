class Menu:
    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = self.get_option()
            self.do_task(choice)
            
            if choice == 0:
                running = False
    
    def print_menu(self):
        pass

    def get_option(self):
        choice = int(input('Enter your choice: '))
        return choice
    
    def do_task(self, choice):
        pass