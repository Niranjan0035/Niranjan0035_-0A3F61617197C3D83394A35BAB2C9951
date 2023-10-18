class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.__account_number = account_number  # Private attribute
        self.__account_holder = account_holder  # Private attribute
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def display_balance(self):
        return f"Account Number: {self.__account_number}\nAccount Holder: {self.__account_holder}\nBalance: {self.__balance}"

# Create an instance of the BankAccount class
my_account = BankAccount("12345", "John Doe", 1000.0)

# Deposit some money
my_account.deposit(500.0)

# Withdraw some money
my_account.withdraw(200.0)

# Display the account balance
print(my_account.display_balance())
