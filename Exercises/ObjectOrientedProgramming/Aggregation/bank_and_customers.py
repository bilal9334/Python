class Customer:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Customer - {self.name} has {self.balance}$ in their bank account"


class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def show_customers(self):
        if not self.customers:
            return f"{self.bank_name} has no customers."
        return f"{self.bank_name} Customers : \n" + "\n".join(str(customer) for customer in self.customers)


if __name__ == '__main__':
    customer1 = Customer("Emmanuel", 10000)
    customer2 = Customer("Bilal", 25000)

    bank = Bank("Sparkasse")

    # add customers to bank
    bank.add_customer(customer1)
    bank.add_customer(customer2)

    print(bank.show_customers())
