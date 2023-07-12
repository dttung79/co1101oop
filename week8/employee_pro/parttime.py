from employee import Employee

class PartTimeEmployee(Employee):
    def __init__(self, name, rate, days):
        super().__init__(name, rate)
        self.__days = days
    
    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self, days):
        if days <= 0:
            raise ValueError("Days must be positive")
        if days > 5:
            raise ValueError("Days must be less than or equal to 5")
        self.__days = days
    
    # Override the salary method
    def salary(self):
        return super().salary() * self.days / 5
    
    def show_info(self):
        super().show_info()
        print('Working days per week:', self.days)