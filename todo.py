import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    if not os.path.isfile(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} [{status}]")

def update_task(tasks, task_index, new_task):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["task"] = new_task
        save_tasks(tasks)
        print(f"Task {task_index + 1} updated to '{new_task}'.")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")

def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_index + 1} marked as completed.")
    else:
        print("Invalid task number.")

def show_menu():
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Complete task")
    print("6. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter a new task: ")
            add_task(tasks, task)
        elif choice == '3':
            task_index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            update_task(tasks, task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '5':
            task_index = int(input("Enter task number to complete: ")) - 1
            complete_task(tasks, task_index)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()