class User:
    """Updates and validates user passwords

    Args:
        __username (str): The username of the user.
        __password (str): The password of the user.

    Methods:
        set_password(): used to set the password of the user.
        check_password(): checks the password if it follows the rules.
    """
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def set_password(self, new_password):
        """Allows the user to update their password"""
        if len(new_password) < 6:
            print("Password to short! Must be at least 6 characters.")
        else:
            self.__password = new_password
            print("Password update successfully")

    def check_password(self, password):
        """Checks if the provided password is correct"""
        if self.__password == password:
            print("Login successful!")
            return True
        else:
            print("Incorrect Password. Try again")
            return False


if __name__ == '__main__':
    user1 = User("Asad", "mySecret123")

    # Trying to check password
    user1.check_password("wrongPass")
    user1.check_password("mySecret123")

    # Updating the password
    user1.set_password("newPass123")

    # Checking with the new password
    user1.check_password("mySecret123")
    user1.check_password("newPass123")

    # Attempting to access private attribute (should not worK)
    try:
        print(user1.__password)
    except AttributeError:
        print("Direct access to password is not allowed! (Encapsulation working)")
