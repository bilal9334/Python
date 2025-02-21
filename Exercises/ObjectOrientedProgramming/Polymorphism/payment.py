class Payment:

    def make_payment(self):
        return "Make Payment with "


class CreditCard(Payment):

    def __init__(self):
        self._credit_card = "Credit Card"

    def make_payment(self):
        return super().make_payment() + self._credit_card


class Paypal(Payment):

    def __init__(self):
        self._paypal = "Paypal"

    def make_payment(self):
        return super().make_payment() + self._paypal


if __name__ == '__main__':
    print("Choose a payment method: ")
    print("1. Credit Card")
    print("2. Paypal")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        payment_method = CreditCard()
    elif choice == "2":
        payment_method = Paypal()
    else:
        print("Invalid choice! Defaulting to Paypal.")
        payment_method = Paypal()

    print(payment_method.make_payment())
