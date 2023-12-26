"""

"""

# To-Do List App without functions and exceptions

# List to store tasks
tasks = []

# Main menu loop
while True:
    # Display menu options
    print("\nMenu:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    # Get user choice
    choice = input("Enter your choice (1-5): ")

    # Display tasks
    if choice == '1':
        if not tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    # Add task
    elif choice == '2':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully.")

    # Delete task
    elif choice == '3':
        task_number = input("Enter the task number to delete: ")
        task_number = int(task_number) if task_number.isdigit() else 0
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task number.")

    # Mark task as completed
    elif choice == '4':
        task_number = input("Enter the task number to mark as completed: ")
        task_number = int(task_number) if task_number.isdigit() else 0
        if 1 <= task_number <= len(tasks):
            completed_task = tasks[task_number - 1]
            tasks[task_number - 1] = f"[Completed] {completed_task}"
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task number.")

    # Exit the program
    elif choice == '5':
        print("Exiting the To-Do List App. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")


#################

# # To-Do List App without functions and exceptions

# # List to store tasks
# tasks = []

# # Main menu loop
# while True:
#     # Display menu options
#     print("\nMenu:")
#     print("1. Display Tasks")
#     print("2. Add Task")
#     print("3. Delete Task")
#     print("4. Mark Task as Completed")
#     print("5. Exit")

#     # Get user choice
#     choice = input("Enter your choice (1-5): ")

#     # Display tasks
#     if choice == '1':


#     # Add task
#     elif choice == '2':


#     # Delete task
#     elif choice == '3':


#     # Mark task as completed
#     elif choice == '4':


#     # Exit the program
#     elif choice == '5':
#         print("Exiting the To-Do List App. Goodbye!")
#         break

#     # Invalid choice
#     else:
#         print("Invalid choice. Please enter a number from 1 to 5.")
