class Employee:
    """Class to manage salary details for employees

    Args:
        __salary (int): The amount that an employee gets each month

    Methods:
        set_salary: Sets the initial salary of an employee
        get_salary: Returns the salary
    """
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print(f"Salary: {amount}")
        else:
            print("Salary cannot be negative")

    def get_salary(self):
        """Return and prints the salary"""
        print(f"{self.name}'s Salary: {self.__salary}")
        return self.__salary


if __name__ == '__main__':
    employee = Employee("Bob", 50000)

    employee.get_salary()
    employee.set_salary(60000)
    employee.get_salary()

    employee.set_salary(-5000)

    try:
        print(employee.__salary) # Should raise an AttributeError
    except AttributeError:
        print("Direct access to attributes is not allowed. (Encapsulation works)")
