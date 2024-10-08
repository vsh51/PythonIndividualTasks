from .tasks import TaskList

class User:
    def __init__(self, name = "Default"):
        self.name = name
        self.tasks = TaskList()

    def add_task(self, data, date):
        self.tasks.add_task(data, date)

    def all_tasks(self):
        return self.tasks.all_tasks()

    def completed_tasks(self):
        return self.tasks.completed_tasks()

    def uncompleted_tasks(self):
        return self.tasks.uncompleted_tasks()

    def remove_task(self, task_id):
        return self.tasks.remove_task(task_id)

    def complete_task(self, task_id):
        for task in self.tasks.tasks:
            if task.task_id == task_id:
                task.complete()
                return True
        raise ValueError("Task not found")

    def uncomplete_task(self, task_id):
        for task in self.tasks.tasks:
            if task.task_id == task_id:
                task.uncomplete()
                return True
        raise ValueError("Task not found")

    def dump(self, file_path):
        with open(f"{file_path}", "w") as f:
            f.write(str(self.tasks) + "\n")

    def __str__(self):
        return f'{self.name}'

class UsersManager:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        self.users.append(User(name))

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        raise ValueError("User not found")
