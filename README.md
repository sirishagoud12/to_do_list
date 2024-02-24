# to_do_list
1.ToDoList class:
  This class serves as the blueprint for the to-do list.
  __init__(self): Initializes an empty list of tasks when an object of the class is created.
  add_task(self, task): Adds a new task to the list with a default status of not completed.
  mark_task_completed(self, index): Marks a task as completed based on its index in the list.
  display_tasks(self): Displays the current list of tasks, indicating whether each task is completed or not.

2.main() function:
  The main entry point of the program.
  Creates an instance of the 'ToDoList' class to manage tasks.
  Utilizes a loop to repeatedly present a menu of options to the user until they choose to quit.
  Options include:Add a new task to the to-do list.
  Mark a task as completed by specifying its index.
  Display the current list of tasks with their completion status.
  Quit the application.

3.User Interaction:
  The user interacts with the program through the console, entering numerical choices corresponding to the menu options.The program takes user input, performs the       requested action, and continues looping until the user decides to quit.

4.Error Handling:
  Basic error handling is implemented, such as checking for invalid menu choices and ensuring the task index is within a valid range before marking it as completed.

5.Execution:
  The if __name__ == "__main__": block ensures that the main() function is executed when the script is run, but not when it's imported as a module.
