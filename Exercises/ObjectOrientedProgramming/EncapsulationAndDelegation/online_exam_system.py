class StudentExam:
    """Class to store exam scores of students in a secure manner

    Args:
        __score (int): The exam score of a student.

    Methods:
        set_score: Updates the score (must be between 0 and 100)
        get_score: Returns the score
    """
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            print("Score updated successfully.")
        else:
            print("Invalid Score! Must be between 0 and 100.")

    def get_score(self):
        print(f"Score: {self.__score}")
        return self.__score


if __name__ == '__main__':
    exam = StudentExam("Bilal", 85)
    exam.get_score()
    exam.set_score(95)
    exam.get_score()

    exam.set_score(120)

    try:
        print(exam.__score)
    except AttributeError:
        print("Direct access to private attribute is not possible. (Encapsulation working)")
