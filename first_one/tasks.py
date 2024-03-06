def display_tasks(tasks):
    print("Your To-Do List:")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully.")

def mark_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

def to_do_list_app():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(tasks, task_index)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    to_do_list_app()
