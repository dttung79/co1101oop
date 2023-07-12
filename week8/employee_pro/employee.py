class Employee:
    def __init__(self, name, rate):
        self.__name = name
        self.__rate = rate
        self._BASIC_SALARY = 1000
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.__name = name
    
    @property
    def rate(self):
        return self.__rate
    
    @rate.setter
    def rate(self, rate):
        if rate <= 0:
            raise ValueError("Rate must be positive")
        self.__rate = rate

    def salary(self):
        return self._BASIC_SALARY * self.rate
    
    def show_info(self):
        print('Name:', self.name, ' salary:', self.salary())