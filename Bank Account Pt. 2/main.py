"""
Main file for bank_account and subclasses
"""

from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    # Two Savings Account instances
    savings_mulder = SavingsAccount("Mulder", curr_balance=5000.0, min_balance=500.0, account_number="SA-1001",
                                   interest_rate=0.04)
    savings_scully = SavingsAccount("Scully", curr_balance=1200.0, min_balance=250.0, account_number="SA-1002",
                                 interest_rate=0.02)

    # Two Checking Account instances
    checking_fox = CheckingAccount("Fox", curr_balance=2500.0, min_balance=100.0, account_number="CA-2001",
                                       transfer_limit=800.0)
    checking_dana = CheckingAccount("Dana", curr_balance=400.0, min_balance=50.0, account_number="CA-2002",
                                    transfer_limit=500.0)

    print("\nTesting deposits and interest...")
    savings_mulder.deposit(1000)
    savings_mulder.apply_interest()

    savings_scully.withdraw(1000)  # Attempt to overdraw below min_balance
    savings_scully.apply_interest()

    print("\nTesting withdrawals and transfer...")
    checking_fox.withdraw(300)

    # Fox attempts to transfer more than allowed by his limit
    checking_fox.transfer(checking_dana, 1000.0)

    # Fox transfers within allowed limit
    checking_fox.transfer(checking_dana, 600.0)

    # Dana tries to transfer more than her balance allows
    checking_dana.transfer(checking_fox, 950.0)

    print("\nTesting cross-account interaction...")
    # Checking account transfer into a savings account
    checking_fox.transfer(savings_scully, 200.0)


if __name__ == "__main__":
    main()