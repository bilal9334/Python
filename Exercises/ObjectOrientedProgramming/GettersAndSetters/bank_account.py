class BankAccount:
    """Validate the balance of an account"""

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self._balance = amount
        else:
            print("Amount should be greater than 0")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must not be negative")

    def withdraw(self, amount):
        if amount > 0 and amount >= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds or invalid amount! ")


if __name__ == '__main__':
    account = BankAccount(100)
    print(account.balance)

    account.deposit(50)
    print(account.balance)

    account.withdraw(100)
    print(account.balance)

    account.withdraw(60)

    account.balance = -500
