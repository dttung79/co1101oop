class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self): 
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def show(self):
        print(f'Name: {self.__name}, Age: {self.__age}')