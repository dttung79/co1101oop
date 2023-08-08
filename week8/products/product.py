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
        if value <= 0:
            raise ValueError('Price must be positive.')
        self.__price = value
    
    # TODO: implement stock property with getter and setter
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError('Stock cannot be negative.')
        self.__stock = value
    
    def get_value(self):
        return self.price * self.stock

class Store:
    def __init__(self):
        self.__products = []
    
    def add(self, p):
        self.__products.append(p)
        print(f'Product {p.name} has been added to the store.')
    
    def remove(self, index):
        if index < -len(self.__products) or index >= len(self.__products):
            raise IndexError('Index out of range.')
        self.__products.pop(index)
    
    def clone_products(self):
        return self.__products[:]
    
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

    def size(self):
        return len(self.__products)