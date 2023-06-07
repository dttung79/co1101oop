class Account:
    def __init__(self, name='Unknown', balance=0, id=0):
        self.__name = name
        self.__balance = balance
        self.__id = id
    
    # read property
    @property
    def name(self):
        return self.__name
    
    # write property
    @name.setter
    def name(self, name):
        if name == '':
            print('Invalid name')
        else:
            self.__name = name
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if id >= 0:
            self.__id = id
        else:
            print('Invalid ID')

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print('Invalid balance')

    def withdraw(self, amount):
        if amount < 0:
            print('Invalid amount. Transaction cancelled')
        elif amount > self.balance:
            print('Not enough balance. Transaction cancelled')
        else:
            self.balance -= amount
            print('Withdraw success. New balance:', self.balance)

    def deposit(self, amount):
        if amount < 0:
            print('Invalid amount. Transaction cancelled')
        else:
            self.balance += amount
            print('Deposit success. New balance:', self.balance)

    def transfer(self, amount, other_account):
        if amount < 0:
            print('Invalid amount. Transaction cancelled')
        elif amount > self.balance:
            print('Not enough balance. Transaction cancelled')
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f'Transfer success. New balance: {self.balance}')

    def show(self):
        print(f'Account id: {self.id}, name: {self.name}, balance: {self.balance}')

