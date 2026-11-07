"""
Bank Account 2.0
Author: Tristan Coleman
"""

class BankAccount:
    title = "Metro Bank"
    __routing_number = "987654321" # Private member denoted by the prefix

    def __init__(self, name, curr_balance, min_balance, account_number):
        self.name = name
        self.curr_balance = curr_balance
        self.min_balance = min_balance
        self._account_number = account_number # Protected member denoted by the prefix

    def routing_number(self):
        """Getter for the private routing number."""
        return self.__routing_number

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
        print(f"Bank is {self.title}")
        print(f"Routing Number is {self.__routing_number}")
        print(f"Account Number is {self._account_number}")
        print(f"Customer is {self.name}")
        print(f"Current balance is ${self.curr_balance:,.2f}")
        print(f"Minimum balance is ${self.min_balance:,.2f}")

