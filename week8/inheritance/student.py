from person import Person

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age) # call the parent's constructor to init name and age
        self.__gpa = gpa
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, gpa):
        self.__gpa = gpa
    
    def show(self):
        super().show()          # call the parent's show method to print name & age
        print(f'GPA: {self.__gpa}')