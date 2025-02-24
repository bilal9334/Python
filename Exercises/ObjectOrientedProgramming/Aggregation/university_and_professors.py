class Professor:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Professor - {self.name} belongs to {self.department} Department"


class University:

    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def list_professor(self):
        if not self.professors:
            return f"{self.name} has not appointed any professors yet"
        return f"{self.name} Professors: \n" + "\n".join(str(professor) for professor in self.professors)


if __name__ == '__main__':

    professor1 = Professor("John Smith", "Mathematics")
    professor2 = Professor("Samantha Joe", "English")
    professor3 = Professor("Abdul Hakim", "Physics")

    university = University("NED University")

    university.add_professor(professor1)
    university.add_professor(professor2)
    university.add_professor(professor3)

    print(university.list_professor())
