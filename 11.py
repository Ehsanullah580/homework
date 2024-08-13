#  Create a class Account with private attributes balance. Provide public methods to deposit and withdraw money.
class Account:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("your balance isn't enough.")
    def get_balance(self):
        return self.__balance
    
ali = Account(30000)
ali.deposit(10000)
ali.withdraw(15000)
print(ali.get_balance())