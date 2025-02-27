class ToDoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task not in self.tasks:
            raise ValueError("Task not found.")
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks[:]
