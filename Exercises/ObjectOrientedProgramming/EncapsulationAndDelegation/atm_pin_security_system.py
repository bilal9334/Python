class ATM:
    """Class to securely manage PIN authentication

    Args:
        __pin (int): The ATM card pin of the account holder.

    Methods:
        set_pin: Updates the PIN
        authenticate: checks if the entered PIN is correct
    """
    def __init__(self, pin):
        self.__pin = pin

    def set_pin(self, new_pin):
        if len(str(new_pin)) != 4:  # checks for the digits if they are 4 digits long
            print("PIN must be 4 digits")
        else:
            self.__pin = new_pin
            print("PIN is of 4 digits")

    def authenticate(self, pin):
        if self.__pin != pin:
            print("Incorrect PIN")
        else:
            print("Access granted")


if __name__ == '__main__':
    atm = ATM(1234)

    atm.authenticate(1111)
    atm.authenticate(1234)

    atm.set_pin(5407)
    atm.authenticate(5407)

    try:
        print(atm.__pin)
    except AttributeError:
        print("Direct access is not allowed. (Encapsulation is working)")
