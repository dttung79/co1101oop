from account import Account

class Bank:
    def __init__(self, name='TP Bank'):
        self.__name = name
        self.__accounts = []  # empty list of accounts
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == '':
            print('Invalid name')
        else:
            self.__name = name
    
    def __get(self, id):
        for acc in self.__accounts:
            if acc.id == id:
                return acc
        return None

    def add(self, acc):
        if self.__get(acc.id) != None:
            print('Account already exists')
        else:
            self.__accounts.append(acc)
            print('Account added')
    
    def withdraw(self, id, amount):
        acc = self.__get(id)
        if acc == None:
            print(f'Account id {id} not found')
        else:
            acc.withdraw(amount)
    
    def deposit(self, id, amount):
        acc = self.__get(id)
        if acc == None:
            print(f'Account id {id} not found')
        else:
            acc.deposit(amount)
    
    def transfer(self, source_id, dest_id, amount):
        source_acc = self.__get(source_id)
        dest_acc = self.__get(dest_id)
        if source_acc == None:
            print(f'Account id {source_id} not found')
        elif dest_acc == None:
            print(f'Account id {dest_id} not found')
        else:
            source_acc.transfer(amount, dest_acc)
    
    def show(self, id):
        acc = self.__get(id)
        if acc == None:
            print(f'Account id {id} not found')
        else:
            acc.show()
    
    def show_all(self):
        for acc in self.__accounts:
            acc.show()