#This Python program creates a to-do list application where users can add tasks, delete tasks,
#mark tasks as completed, and display their current tasks.

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        del self.tasks[index]

    def mark_completed(self, index):
        self.tasks[index]["completed"] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "[X]" if task["completed"] else "[ ]"
                print(f"{i + 1}. {status} {task['task']}")


def to_do_list():
    todo_list = TodoList()
    while True:
        print("\nTODO List")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            if (0 <= index < len(todo_list.tasks)):
                todo_list.delete_task(index)
            else:
                print("Invalid task number.")
        elif choice == "3":
            todo_list.display_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.mark_completed(index)
            else:
                print("Invalid task number.")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    to_do_list()
