from product import Product, Store

class StoreProgram:
    def __init__(self, store):
        self.store = store
    
    def print_menu(self):
        print('1. Add product')
        print('2. Remove product')
        print('3. Show all products')
        print('4. Find product')
        print('5. Find empty products')

    def get_option(self):
        while True:
            option = int(input('Enter option: '))
            if option >= 1 and option <= 5:
                return option
            print('Invalid option. Try again.')
    
    def do_task(self, option):
        if option == 1:
            name = input('Enter product name: ')
            price = float(input('Enter product price: '))
            stock = int(input('Enter product stock: '))
            product = Product(name, price, stock)
            self.store.add(product)
        elif option == 2:
            name = input('Enter product name to remove: ')
            self.store.remove(name)
        elif option == 3:
            self.store.show_all()
        elif option == 4:
            name = input('Enter product name to find: ')
            products = self.store.find(name)
            if len(products) == 0:
                print(f'Product {name} not found.')
            else:
                print(f'Found {len(products)} products.')
                for p in products:
                    p.show_info()
        elif option == 5:
            empty_products = self.store.find_empty()
            if len(empty_products) == 0:
                print('No empty products.')
            else:
                print(f'Found {len(empty_products)} empty products.')
                for p in empty_products:
                    p.show_info()
    
    def run(self):
        while True:
            self.print_menu()
            option = self.get_option()
            self.do_task(option)


#### MAIN PROGRAM ####
store = Store()
program = StoreProgram(store)
program.run()