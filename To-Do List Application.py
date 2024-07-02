# Personal Notes: I know that I need to make it so that my "menu" pops up at each interval but I couldn't figure it out
# Additionally, I didn't see a reason or way to use a "finally" block since it was relatively okay


# Define a Task class to represent individual tasks
class Task:
    def __init__(self, title):
        self.title = title  # Initialize task title
        self.completed = False  # Initialize task as not completed
tasks = []  # Initialize an empty list to store Task objects
# Function to display the main menu options
def display_menu():
    print("\nWelcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
# Function to add a new task to the list
def add_task():
    title = input("Enter task name: ")  # Prompt user for task name
    task = Task(title)  # Create a new Task object
    tasks.append(task)  # Add the Task object to the tasks list
    print(f'"{title}" task added successfully.')
# Function to display all tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks.")  # If tasks list is empty, print message
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Complete" if task.completed else "Incomplete"
            print(f"{index}. {task.title} - {status}")  # Display task title and completion status
# Function to mark a task as complete
def mark_complete():
    view_tasks()  # Display current tasks to the user
    try:
        task_index = int(input("Enter task number to mark as complete: ")) - 1  # Prompt user for task number
        if 0 <= task_index < len(tasks):
            tasks[task_index].completed = True  # Mark the selected task as completed
            print(f'Task "{tasks[task_index].title}" marked as complete.')
        else:
            print("Invalid task number.")  # If user enters invalid task number, print message
    except ValueError:
        print("Invalid input. Please enter a number.")  # If user enters non-numeric input, print message
# Function to delete a task from the list
def delete_task():
    view_tasks()  # Display current tasks to the user
    try:
        task_index = int(input("Enter task number to delete: ")) - 1  # Prompt user for task number
        if 0 <= task_index < len(tasks):
            del tasks[task_index]  # Delete the selected task from the tasks list
            print("Task deleted.")
        else:
            print("Invalid task number.")  # If user enters invalid task number, print message
    except ValueError:
        print("Invalid input. Please enter a number.")  # If user enters non-numeric input, print message
# Main function that controls the flow of the program
def main():
    display_menu()  # Display the main menu options
    while True:
        try:
            choice = int(input("Enter your choice: "))  # Prompt user for menu choice
            if choice == 1:
                add_task()  # Call add_task function if user chooses option 1
            elif choice == 2:
                view_tasks()  # Call view_tasks function if user chooses option 2
            elif choice == 3:
                mark_complete()  # Call mark_complete function if user chooses option 3
            elif choice == 4:
                delete_task()  # Call delete_task function if user chooses option 4
            elif choice == 5:
                print("Thank you for using the To-Do List App.")
                break  # Exit the loop and end the program if user chooses option 5
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")  # If user enters non-numeric input, print message
# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the program