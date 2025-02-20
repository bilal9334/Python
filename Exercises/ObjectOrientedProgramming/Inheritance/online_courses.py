class Course:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def display_details(self):
        return "Title: {0.title}, Duration: {0.duration} hours".format(self)


class OnlineCourse(Course):

    def __init__(self, title, duration, platform):
        super().__init__(title, duration)
        self.platform = platform

    def display_details(self):
        return "Title: {0.title}, Duration: {0.duration} hours, Platform: {0.platform}".format(self)


if __name__ == '__main__':

    c1 = OnlineCourse("Python", 6, "Udemy")
    print(c1.display_details())

    c2 = OnlineCourse("Spring Boot", 3, "Coursera")
    print(c2.display_details())
