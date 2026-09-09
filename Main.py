#code that is repeated can be simplified to a function that will be called when needed for making the program easier to read
import sys

tasks = []
nb_of_actions = 3

def display_menu():
    print("""
=========================

1. Add Task
2. View Tasks
3. Remove Task

=========================
""")


def add_task(new_task):
    tasks.append(new_task)

def remove_task(new_task):
    found = False
    for task in tasks:
        if task == new_task:
            tasks.remove(task)
            found = True
            break

    if found == True:
        print("Task removed successfully!")
    else:
        print("Task not found.")


while True: 
    display_menu() 
    try:
        action = int(input("Choose a number representing the action u would like to perform from the menu (1-3) : "))

    except ValueError as error:
        print(f"{error} Try again")
        continue

    if not 1 <= action <= nb_of_actions:
        print("You entered an invalid integer. Try again")
        continue

    elif action == 1:    
        new_task = input("What task do u wanna add : ")    #see different ways to handle text input from user, example accept is user enters Add task, add Task, Add Task, ... , here we cant use lower() or upper() so either use lst with tolerance writings, or some Python function exists or Ican create a loop that goes through all characters of theuser input and acts on first letter of every word
        add_task(new_task)
        print(f"{new_task} was successfully added")
        

    elif action == 2:
        for index, task in enumerate(tasks, start=1):
            print(index, task)
        print(f"Nb of tasks : {len(tasks)}")
        

    elif action == 3:
        task = input("What task do u wanna remove : ")    
        remove_task(task)
        

    while True:
        other_action = input("Do u wanna perform an other action? ").lower().strip()

        if other_action == "yes":
            break

        elif other_action == "no":
            print("Ok, goodbye")
            sys.exit()

        else:
            print("You entered invalid input. Try again!")
            continue    

    


