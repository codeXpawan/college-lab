class Bank_Account:
    def __init__(self, balance, account_number) -> None:
        self.__balance = balance
        self._account_number = account_number
    
    def deposit(self,amount):
        self.__balance += amount
        print(f'Available Balance : {self.__balance}')
        
    def withdraw(self,amount):
        self.__balance -= amount
        print(f'Available Balance : {self.__balance}')
    
my_account = Bank_Account(999999999,90910897937)
my_account.deposit(20000)
my_account.withdraw(10000)
# print(my_account.__balance) #shows AttributeError
print(my_account._account_number) #can be accessed