class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Price: {self.price}')
        print(f'Stock: {self.stock}')
    
    def get_value(self):
        return self.price * self.stock

class Store:
    def __init__(self):
        self.products = []
    
    def add(self, p):
        self.products.append(p)
        print(f'Product {p.name} has been added to the store.')
    
    def remove(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f'Product {p.name} has been removed from the store.')
                return
        print(f'Product {name} not found.')
    
    def show_all(self):
        if len(self.products) == 0:
            print('No product in the store.')
            return
        
        for p in self.products:
            p.show_info()
        
    
    def find(self, name):
        found_products = []
        for p in self.products:
            if p.name == name:
                print(f'Found product {p.name} in the store.')
                found_products.append(p)
        
        return found_products
    
    def find_empty(self):
        empty_products = []
        for p in self.products:
            if p.stock == 0:
                empty_products.append(p)
        
        return empty_products