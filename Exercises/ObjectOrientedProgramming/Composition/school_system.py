class Student:

    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    def check_grade(self):
        if self._grade == "F":
            return "You Failed!"
        else:
            return "You Passed!"

    def __str__(self):
        return f"Student Data - Name of Student: {self._name}, Age: {self._age}, Grade: {self._grade}"


class Teacher:

    def __init__(self, name, subject, experience):
        self._name = name
        self._subject = subject
        self._experience = experience

    def __str__(self):
        return (f"Teacher Data - Name of Teacher: {self._name}, Subject: {self._subject}, Experience: "
                f"{self._experience}"
                f" Years")


class School:

    def __init__(self):
        self._students = []
        self._teachers = []

    def add_student(self, student):
        self._students.append(student)

    def add_teacher(self, teacher):
        self._teachers.append(teacher)

    def list_students(self):
        if not self._students:
            print("No students enrolled yet")
        else:
            print("Students in the School")
            for student in self._students:
                print(student, "-", student.check_grade())

    def list_teachers(self):
        if not self._teachers:
            print("No teachers available")
        else:
            print("Teachers in School")
            for teacher in self._teachers:
                print(teacher)


if __name__ == '__main__':
    student1 = Student("Joe", 12, "A")
    student1.check_grade()
    student2 = Student("Bob", 14, "B")
    student3 = Student("Alice", 15, "F")

    teacher1 = Teacher("Henry Smith", "Math", 5)
    teacher2 = Teacher("Laura Jones", "English", 8)

    school = School()

    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)
    school.list_students()
    school.list_teachers()
