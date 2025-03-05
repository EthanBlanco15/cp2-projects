#Ethan Blanco, To Do List Notes

#Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file. 
#REQUIREMENTS:
#Create the to do list (Kept on a txt file)
#Add items to the to do list
#Mark item as complete
#Delete item from to do list

import os

#Define file path, notes\to_do_list.txt
folder = "to_do_list.py"
file_name = "to_do_list.txt"
file_path = os.path.join(folder, file_name)

#Ensure the folder and file exist
if not os.path.exists(folder):
    os.makedirs(folder)

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        pass  #Create an empty file

def load_tasks():
    #Load tasks from file into a list.
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    #Save the list of tasks to the file.
    with open(file_path, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks():
    #Display the to-do list.
    tasks = load_tasks()
    if not tasks:
        print("\nTo-Do List is empty!\n")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task():
    #Add a task to the to-do list.
    task = input("Enter the new task: ")
    if task:
        tasks = load_tasks()
        tasks.append("[ ] " + task)  #Unmarked task
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Task can't be empty!\n")

def mark_task_complete():
    #Mark a task as complete.
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks to mark as complete!\n")
        return
    
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark complete: ")) - 1
        if 0 <= task_num < len(tasks):
            if tasks[task_num].startswith("[X]"):
                print("Task was already completed!\n")
            else:
                tasks[task_num] = "[X]" + tasks[task_num][3:]
                save_tasks(tasks)
                print("Task is complete!\n")
        else:
            print("Wrong task number!\n")
    except ValueError:
        print("This didn't work, please enter a number.\n")

def delete_task():
    #Delete a task from the to-do list.
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks to delete!\n")
        return
    
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            save_tasks(tasks)
            print("Task deleted.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

def main():
    #Main loop to run the to-do list program.
    while True:
        print("To-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("This doesn't work, try to enter a number between 1-5 next time.\n")
    main()