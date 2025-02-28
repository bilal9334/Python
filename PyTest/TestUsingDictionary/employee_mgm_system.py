class EmployeeManager:

    def __init__(self):
        self.employees = {}

    def add_employee(self, name, salary):
        if name in self.employees:
            raise ValueError("Employee already exists.")
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.employees[name] = salary

    def remove_employee(self, name):
        if name not in self.employees:
            raise KeyError("Employee not found")
        del self.employees[name]

    def update_salary(self, name, salary):
        if name not in self.employees:
            raise KeyError("Employee not found")
        if salary < 0:
            raise KeyError("Salary cannot be negative")
        self.employees[name] = salary

    def get_salary(self, name):
        if name not in self.employees:
            raise KeyError("Employee not found")
        return self.employees[name]

    def get_all_employees(self):
        return self.employees.copy()
