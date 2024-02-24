class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid index")
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = " [X] " if task["completed"] else " [ ] "
                print(f"{i + 1}.{status}{task['task']}")
def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Tasks")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
