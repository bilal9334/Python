class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def display_balance(self):
        return "Current Balance: {0.balance}".format(self)

    def apply_interest(self, rate):
        self.balance += self.balance * rate


class SavingAccount(BankAccount):

    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self, rate=None):
        if rate is None:
            rate = self.interest_rate
        self.balance += self.balance * rate


if __name__ == '__main__':
    account = SavingAccount("Bilal", 3000, 0.05)
    account.deposit(1000)
    account.apply_interest()
    account.withdraw(500)
    print(account.display_balance())

    print()

    account.apply_interest(0.07)
    print(account.display_balance())
