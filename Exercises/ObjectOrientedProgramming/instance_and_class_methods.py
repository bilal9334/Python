class BankAccount:
    """Simple class to show Account Information"""

    @staticmethod
    def _interest_rate():
        rate = 0.05
        return rate

    @classmethod
    def bank_policy(cls, amount=100):
        print(f"Minimum balance required: {amount}")
        print(f"Bank Interest Rate: {BankAccount._interest_rate()}")

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount!")

    def show_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")


if __name__ == '__main__':
    person_account = BankAccount("John", 500)
    person_account.show_balance()
    person_account.bank_policy()
