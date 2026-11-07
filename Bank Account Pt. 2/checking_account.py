"""
Checking Account 1.0
"""

from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, name, curr_balance, min_balance, account_number, transfer_limit=1000.0):
        super().__init__(name, curr_balance, min_balance, account_number)
        self.transfer_limit = transfer_limit

    def transfer(self, target_account, amount):
        """Take amount from caller's account and give to target account"""
        if amount <= 0:
            print("Error: Transfer amount must be positive.")
            return

        if amount > self.transfer_limit:
            print(f"Transfer failed: ${amount} exceeds per-transfer limit of ${self.transfer_limit:,.2f}.")
            return

        if self.curr_balance - amount < self.min_balance:
            print(f"Transfer failed: Insufficient funds. Minimum balance required is ${self.min_balance:,.2f}.")
            return

        self.curr_balance -= amount
        target_account.curr_balance += amount
        print(f"Transfer successful: ${amount} transferred from {self.name} to {target_account.name}.")
        print(f"{self.name}'s new balance: ${self.curr_balance:,.2f}")

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Transfer Limit is ${self.transfer_limit:,.2f}")