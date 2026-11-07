"""
Savings Account 1.0
"""

from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, curr_balance, min_balance, account_number, interest_rate=0.03):
        super().__init__(name, curr_balance, min_balance, account_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Adds interest to balance and prints earnings"""
        interest_earned = self.curr_balance * self.interest_rate
        self.curr_balance += interest_earned
        print(f"{self.name} earned ${interest_earned} interest.")

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Interest Rate is {self.interest_rate * 100:.1f}%")