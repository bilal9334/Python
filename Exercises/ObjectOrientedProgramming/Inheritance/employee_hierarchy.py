class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, task):
        super().__init__(name, salary)
        self.task = task

    def assign_task(self):
        return "Name of Employee: {0.name}, Task: {0.task}, Salary: {0.salary}".format(self)


if __name__ == '__main__':
    e1 = Manager("Bob", 10000, "Print the papers")
    print(e1.assign_task())

    e2 = Manager("Emmanuel", 4300, "Write Requirements")
    print(e2.assign_task())
