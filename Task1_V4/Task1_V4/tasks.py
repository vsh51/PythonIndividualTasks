class Task:
    # Autoincrement id
    _task_id = 0

    def __init__(self, data, date):
        self.task_id = Task._task_id
        Task._task_id += 1

        self.title = data['title']
        self.description = data['description']
        self.date = date

        self.completed = False

    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.completed = False

    def __str__(self):
        return f"{self.task_id} | {self.title} | {self.description} | {self.date} | " \
                f"{'Completed' if self.completed else 'Uncompleted'}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, data, date):
        self.tasks.append(Task(data, date))

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def all_tasks(self):
        return self.tasks

    def completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __str__(self):
        strgified_tasks = [str(task) for task in self.tasks]
        return "[]" if len(strgified_tasks) == 0 else "\n".join(strgified_tasks)
