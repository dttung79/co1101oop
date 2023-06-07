class Student:
    def __init__(self, name='Unknown', id=0, gpa=0.0):
        self.name = name # public attribute
        self.__id = id   # private attribute
    
    def get_id(self): # accessor method to provide read access
        return self.__id

    def set_id(self, id): # mutator method to provide write access
        if id >= 0:
            self.__id = id
        else:
            print('Invalid ID')
    
    def show(self):
        print('Name:', self.name)
        print('ID:', self.__id)
    

john = Student('John', 1, 3.5)
john.show()

john.name = 'John Lennon' # (write access) ok because name is public
print(john.name)        # (read access) ok because name is public
#john.__id = 2 # Error: cannot access private member __id    (write access)
#print(john.__id) # Error: cannot access private member __id (read access)

john.set_id(2) # (write access) ok because set_id() is public
print(john.get_id()) # (read access) ok because get_id() is public

john.set_id(-100)
print(john.get_id())