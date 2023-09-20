todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})

def view_tasks():
    for index, task in enumerate(todo_list, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['task']} - {status}")


def mark_completed(task_index):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["completed"] = True
    else:
        print("Invalid task index.")


def remove_task(task_index):
    if 1 <= task_index <= len(todo_list):
        del todo_list[task_index - 1]
    else:
        print("Invalid task index.")

def clear_tasks():
    global todo_list
    todo_list = []
    print("All tasks have been cleared.")


#main
while True:
 print("TO DO LIST")
 print("1. SHOW LIST")
 print("2. Mark Task as Completed")
 print("3. ADD TO LIST")
 print("4. REMOVE FROM LIST")
 print("5. CLEAR LIST")
 print("6. EXIT")
 X=input("GIVE OPTION :")
 if X == "1":
        view_tasks()
 elif X == "2":
        task_index = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_index)
 elif X == "3":
        task = input("Enter a task: ")
        add_task(task)
        
 elif X == "4":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
 elif X == "5":
        print("THE LIST IS CLEAR")
        clear_tasks()
 elif X == "6":
        break   
 else:
        print("Invalid choice. Please try again.")
