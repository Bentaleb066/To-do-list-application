import json
from pathlib import Path
tasks = []

with open(Path("tasks.json"), "r") as file:
    tasks = json.load(file)


nb_of_actions = 5
running = True

def display_menu():
    print("""
        MENU
====================

1. Add Task
2. View Tasks
3. Remove Task
4. Complete task
5. Exit

====================
""")


def add_task(new_task):  #deal with empt string as a task
    tasks.append(new_task)
    print(f"'{new_task}' was successfully added")

def remove_task(new_task):  #deal with empt string as a task
    found = False
    for task in tasks:
        if task == new_task:
            tasks.remove(task)
            found = True
            break
    if found == True:
        print(f"'{new_task}' was removed successfully!")
    else:
        print(f"'{new_task}' was not found.")

def view_tasks():

    print("Your tasks : ")

    for index, task in enumerate(tasks, start=1):
        if task["completed"] == True:
            print(f"{index}. [✓]  {task['task']}")

        elif task["completed"] == False:
            print(f"{index}. [ ]  {task['task']}")

    print(f"Nb of tasks : {len(tasks)}")

def complete_task():
    view_tasks()
    task_to_complete = input("Choose a task to complete from the list of tasks : ")
    for task in tasks:
        if task["completed"] == False and task_to_complete == task["task"]:
            task["completed"] = True
            print(f"'{task_to_complete}' has been successfully marked as completed")
            with open(Path("tasks.json"), "w") as file:
                json.dump(tasks, file)
            
            

while running: 
    display_menu() 

    try:
        action = int(input(f"Choose a number representing the action u would like to perform from the menu (1-{nb_of_actions}) : "))

    except ValueError as error:
        print(f"{error} Try again. ")
        continue

    if not 1 <= action <= nb_of_actions:
        print("You entered an invalid integer. Try again.")
        continue

    elif action == 1:   
        new_task = input("What task do u wanna add?  : ") 
        add_task(new_task)

    elif action == 2:
        view_tasks()    

    elif action == 3:
        new_task = input("What task do u wanna remove? : ")    
        remove_task(new_task)

    elif action == 4:
        complete_task()

    elif action == 5:
        print("Goodbye")
        with open(Path("tasks.json"), "w") as file:
            json.dump(tasks, file)
        break
                
            
    


