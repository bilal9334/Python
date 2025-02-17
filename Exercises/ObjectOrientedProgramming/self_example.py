class Student:
    """A class to show grade of a student or students"""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        if self.grade >= 50:
            print(f"{self.name} has passed with a grade of {self.grade}")
            return True
        else:
            print(f"{self.name} is failed! Try again in the next term")
            return False


if __name__ == '__main__':
    student1 = Student("Asad", 100)
    student1.is_passing()
    student2 = Student("Bob", 20)
    student2.is_passing()
