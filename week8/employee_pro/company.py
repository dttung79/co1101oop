from employee import Employee
from parttime import PartTimeEmployee

class Company:
    def __init__(self, name='FPT'):
        self.__name = name
        self.__full_times = []
        self.__part_times = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.__name = name
    
    def add_full(self, emp):
        # check if emp is an instance of Employee
        if not isinstance(emp, Employee):
            raise ValueError("Must be an instance of Employee")
        
        self.__full_times.append(emp)

    def add_part(self, emp):
        if not isinstance(emp, PartTimeEmployee):
            raise ValueError("Must be an instance of PartTimeEmployee")
        
        self.__part_times.append(emp)
    
    def show_employees(self):
        print('Full time employees:')
        for e in self.__full_times:
            e.show_info()
        print('Part time employees:')
        for e in self.__part_times:
            e.show_info()