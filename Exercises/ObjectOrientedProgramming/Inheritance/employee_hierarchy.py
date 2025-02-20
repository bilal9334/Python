class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return "Name: {0.name}, Salary: {0.salary}".format(self)


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name=name, salary=salary)
        self.programming_language = programming_language

    def show_details(self):
        return super().show_details() + ", Programming Language: {0.programming_language}".format(self)


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_details(self):
        return super().show_details() + ", Team Size: {0.team_size}".format(self)


if __name__ == '__main__':
    dev1 = Developer("Emmanuel", 4300, "C++")
    print(dev1.show_details())

    dev2 = Developer("Bilal", 4300, "Python")
    print(dev2.show_details())

    manager = Manager("Susanne", 10000, 20)
    print(manager.show_details())
