students = {
    "Alice": {"Math": 90, "English": 85},
    "Bob": {"Math": 78, "English": 82},
    "Charlie": {"Math": 88, "English": 90}
}

for student, subjects in students.items():
    for subject, grade in subjects.items():
        print(f"{student} scored {grade} in {subject}")
    