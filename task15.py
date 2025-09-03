class Todolist:
    def __init__(self,):
        self.Tasks = []

    def add_task(self, task):
        self.Tasks.append(task)


    def show_tasks(self):
        for i, task in enumerate(self.Tasks, start=1):
            print(f"{i}. {task}")
            

todo = Todolist()
todo.add_task("Do homework")
todo.add_task("Clean room")
todo.show_tasks()


