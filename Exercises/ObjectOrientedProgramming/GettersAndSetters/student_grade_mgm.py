class Student:
    """Manages the grades of students and returns the result"""

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, score):
        if 0 <= score <= 100:
            self._grade = score
        else:
            print("Grade must be between 0 and 100!")

    @property
    def status(self):
        if self._grade >= 50:
            return "Pass"
        else:
            return "Fail"


if __name__ == '__main__':
    student = Student("Ali", 85)
    print(student.grade)
    print(student.status)

    student.grade = 45
    print(student.status)

    student.grade = 120
