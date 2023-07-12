# Write a menu program with following options:
# 1. Add full time employee (ask for name and rate)
# 2. Add part time employee (ask for name, rate and days)
# 3. Show all employees
# 0. Quit
# Program runs until user chooses to quit.

from menu import Menu
from company import Company
from employee import Employee
from parttime import PartTimeEmployee

class CompanyProgram(Menu):
    def __init__(self, name='FPT'):
        self.__company = Company(name)
    
    def print_menu(self):
        print('1. Add full time employee')
        print('2. Add part time employee')
        print('3. Show all employees')
        print('0. Quit')

    def do_task(self, choice):
        if choice == 1:
            self.__add_full()
        elif choice == 2:
            self.__add_part()
        elif choice == 3:
            self.__company.show_employees()
        elif choice == 0:
            print('Thank you for using our program')
        else:
            print('Invalid option')

    
    def __add_full(self):
        name = input('Enter name: ')
        rate = float(input('Enter rate: '))
        emp = Employee(name, rate)
        self.__company.add_full(emp)

    def __add_part(self):
        name = input('Enter name: ')
        rate = float(input('Enter rate: '))
        days = int(input('Enter days: '))
        emp = PartTimeEmployee(name, rate, days)
        self.__company.add_part(emp)
    

program = CompanyProgram()
program.run()