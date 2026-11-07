"""
Bank Account Class 2.0
Author: Tristan Coleman
"""

class BankAccount:
    title = "Metro Bank"

    def __init__(self, name, curr_balance, min_balance):
        self.name = name
        self.curr_balance = curr_balance
        self.min_balance = min_balance

    def deposit(self, amount):
        """Add to balance & print amount deposited"""
        self.curr_balance += amount
        print(self.name,"deposited $" + str(amount))

    def withdraw(self, amount):
        """Subtract from balance and print amount withdrawn"""
        if self.curr_balance - amount < self.min_balance:
            print("Error: ",self.name,"attempted to overdraw")
        else:
            self.curr_balance -= amount
            print(self.name,"withdrew $" + str(amount))

    def print_customer_information(self):
        print("Retrieving Customer Information...")
        print("Bank is", self.title)
        print("Customer is",self.name)
        print("Current balance is $" + str(self.curr_balance))
        print("Minimum balance is $" + str(self.min_balance))

account_1 = BankAccount("Tom", 500, 200)
account_2 = BankAccount("Jerry", 1400, 400)

account_1.deposit(100)
account_1.withdraw(600)

account_2.deposit(500)
account_2.withdraw(200)

account_2.print_customer_information()

