def total_score(student_name: str, students: dict) -> int:
    if student_name in students:
        return sum(students[student_name].values())
    else:
        return "Student not found"

def add_student(student_name: str, subject_score: dict, students: dict) -> dict:
    students[student_name] = subject_score
    return students

def find_score(student_name: str, subject: str, students: dict) -> str:
    if student_name in students:
        if subject in students[student_name]:
            return students[student_name][subject]
        else:
            return "Student not found"
    else:
        return "Student not found"


students = {
    "Alice": {"Math": 90, "English": 85},
    "Bob": {"Math": 78, "English": 82},
    "Charlie": {"Math": 88, "English": 90}
}

score = total_score("Bob", students)
print(score)

new_student = {"Math": 90, "Urdu": 85}
studnets = add_student("David", new_student, students)
print(students)

print(find_score("Alice", "Math", students))