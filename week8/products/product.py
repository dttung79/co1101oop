class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError('Name cannot be empty.')
        self.__name = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        # TODO: validate value must be a positive number
        self.__price = value
    
    # TODO: implement stock property with getter and setter
    
    def get_value(self):
        return self.price * self.stock

class Store:
    def __init__(self):
        self.__products = []
    
    def add(self, p):
        self.__products.append(p)
        print(f'Product {p.name} has been added to the store.')
    
    def remove(self, name):
        for p in self.__products:
            if p.name == name:
                self.__products.remove(p)
                print(f'Product {p.name} has been removed from the store.')
                return
        print(f'Product {name} not found.')
    
    # operator [], give access to product at index
    def __getitem__(self, index):
        n = len(self.__products)
        if index < -n or index >= n:
            raise IndexError('Index out of range.')
        
        return self.__products[index]    
    
    def find(self, name):
        found_products = []
        for p in self.__products:
            if p.name == name:
                found_products.append(p)
        
        return found_products
    
    def find_empty(self):
        empty_products = []
        for p in self.__products:
            if p.stock == 0:
                empty_products.append(p)
        
        return empty_products