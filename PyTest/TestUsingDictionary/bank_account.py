class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def transfer(self, amount, recipient_account):
        if not isinstance(recipient_account, BankAccount):
            raise TypeError("Recipient must be BankAccount instance")
        self.withdraw(amount)
        recipient_account.deposit(amount)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account: {self.account_number}; Balance: {self.balance:.2}"
