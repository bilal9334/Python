class InterestCalculator:
    """Handles interest calculation separately"""

    @staticmethod
    def calculate(balance, rate=0.05):
        return balance * rate


class BankAccount:
    """Simple class to show Account Information"""

    @classmethod
    def bank_policy(cls, amount=100):
        print(f"Minimum balance required: {amount}")

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.interest_calculator = InterestCalculator()

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

    def add_interest(self):
        """Delegates interest calculation to InterestCalculator"""
        interest = self.interest_calculator.calculate(self.balance)
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")


if __name__ == '__main__':
    person_account = BankAccount("John", 500)
    person_account.show_balance()
    person_account.bank_policy()

    print()

    person_account.deposit(500)
    person_account.withdraw(200)
    person_account.add_interest()  # Add interest (delegated)
