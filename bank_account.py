class BankAccount:
    def __init__(self, account_name, account_number, account_balance):
        self.name = account_name
        self.number = account_number
        self.balance = account_balance

    def check_balance(self):
        print(f"Your current balance is ${self.balance}. ")

    def deposit_money(self, money):
        # Add the deposited money to the current balance
        self.balance += money
        print(f"${money} has been added to your account {self.number}. ")
        # Check the updated balance
        self.check_balance()

    def withdraw_money(self, money):
        # Check if there is sufficient balance to withdraw
        if self.balance >= money:
            self.balance -= money
            print(f"${money} has been deducted from your account {self.number}. ")
        else:
            print("Insufficient balance!")
        # Check the updated balance
        self.check_balance()


# Get the account name from the user
account_name = input("What's your Account Name? ")
print(f"Hello {account_name}! ")

# Get the account number from the user
account_number = int(input("What's your Account Number? "))

# Get the account balance from the user
account_balance = float(input("What's your Account balance? "))

# Create a BankAccount object
bank_account = BankAccount(account_name, account_number, account_balance)

# Check the initial balance
bank_account.check_balance()

# Deposit money
bank_account.deposit_money(3000)
