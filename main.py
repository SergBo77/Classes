class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = True

class TasksList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = False
                break

    def list_tasks(self):
        current_tasks = [task for task in self.tasks if task.status]
        for task in current_tasks:
            print(f"Описание задачи: {task.description}, Срок выполнения: {task.deadline}, Статус: {task.status}")


tasks = TasksList()

task1 = Task("Позвонить врачу", "15.04.2024")
task2 = Task("Сделать презентацию", "16.04.2024")
task3 = Task("Сходить в магазин", "17.04.2024")

tasks.add_task(task1)
tasks.add_task(task2)
tasks.add_task(task3)

tasks.mark_task_done("Позвонить врачу")

tasks.list_tasks()