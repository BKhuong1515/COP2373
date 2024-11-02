# Name: Brandon Nguyen
# Date Created: 10/30/24
# Assignment: Exercise 9A

# This program defines a BankAcct class that updates the interest rate,
# depositing, withdrawing, checking balance,
# and calculating interest over a given number of days.

class BankAcct:
    def __init__(self, holder_name, acct_number, balance=0.0, annual_interest=0.0):
        # Initialize the bank account with name, account number, balance, and interest rate.
        self.holder_name = holder_name
        self.acct_number = acct_number
        self.balance = balance
        self.annual_interest = annual_interest

    def update_interest_rate(self, new_interest_rate):
        # Update the interest rate for the account if valid (0 to 1).
        if 0 <= new_interest_rate <= 1:
            self.annual_interest = new_interest_rate
            print(f"Interest rate updated to {new_interest_rate:.2%}")
        else:
            print("Invalid interest rate. Please enter a rate between 0 and 1.")

    def deposit_funds(self, amount):
        # Deposit the specified amount if it's positive.
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw_funds(self, amount):
        # Withdraw the specified amount if it does not exceed the balance.
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_current_balance(self):
        # Return the current balance of the account.
        return self.balance

    def calculate_daily_interest(self, days):
        # Calculate the interest earned over a specified number of days if positive.
        if days > 0:
            daily_interest_rate = self.annual_interest / 365
            interest_earned = self.balance * daily_interest_rate * days
            return interest_earned
        else:
            print("Number of days must be positive.")
            return 0

    def __str__(self):
        # Display the account holder's name, account number, balance, and interest rate.
        return (
            f"Account Holder: {self.holder_name}\n"
            f"Account Number: {self.acct_number}\n"
            f"Current Balance: ${self.balance:.2f}\n"
            f"Annual Interest Rate: {self.annual_interest:.2%}\n"
        )


def test_bank_acct():
    # Initialize account with starting balance and interest rate
    initial_balance = 10000.0
    initial_interest_rate = 0.07
    test_account = BankAcct(
        holder_name="John Doe",
        acct_number="12345678",
        balance=initial_balance,
        annual_interest=initial_interest_rate
    )

    # Display initial account details
    print("Account Information:")
    print(test_account)

    # Update the interest rate
    updated_interest_rate = 0.035
    print(f"\nUpdating interest rate to {updated_interest_rate * 100}%")
    test_account.update_interest_rate(new_interest_rate=updated_interest_rate)
    print(test_account)

    # Deposit an amount
    deposit_amount = 750
    print(f"\nDepositing ${deposit_amount} into account: {test_account.acct_number}")
    test_account.deposit_funds(amount=deposit_amount)
    print(test_account)

    # Withdraw an amount
    withdrawal_amount = 300
    print(f"\nWithdrawing ${withdrawal_amount} from account: {test_account.acct_number}")
    test_account.withdraw_funds(amount=withdrawal_amount)
    print(test_account)

    # Display current balance
    print("\nCurrent balance:", test_account.get_current_balance())

    # Calculate interest for a specific period
    days = 45
    print(f"\nCalculating interest for {days} days...")
    interest = test_account.calculate_daily_interest(days=days)
    print(f"Interest earned over {days} days: ${interest:.2f}")


# Run the test function
test_bank_acct()
