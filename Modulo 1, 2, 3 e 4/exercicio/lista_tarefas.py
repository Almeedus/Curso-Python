from os import system

def create_list(list_todo=None):
    if list_todo == None:
        list_todo = []
    return list_todo

def add_task(task=str, todo_list=None):
    if todo_list is None:
        create_list(todo_list)
    todo_list.append(task)
    return todo_list

def remove_last_task(list_remove=None, list_add=None):
    if list_remove == None:
        create_list(list_remove)
    if list_add == None: 
        create_list(list_add)
    
    try:
        task = list_remove[-1]
        list_add.append(task)
        list_remove.remove(task)
        return print(f'{str(task).upper()} successfully redone.\n')
        
    except IndexError:
        print(_red[0],"The list is already empty.",_red[1])
        input("Type enter to reload.")
        system("clear")
        
    
_red = ["\033[31m","\033[m"]
list_task = []
backup_task_list = []
while True:
    option_list = ["Add task", "Undo task", "Redo task", "Visualize List"]
    
    print("To-do list:")
    for _index, option in enumerate(option_list):
        print("[{}] - {}".format(_index+1, option))

    print("Choose an option.")
    
    try:
        user_choose = input()
        user_choose = int(user_choose)-1
        
    except ValueError:
        
        print(_red[0],"Wrong value! Type only numbers.",_red[1])
        input("Type enter to reload.")
        system("clear")
        continue
    
    if user_choose == 0:
        system("clear")
        task_user = str(input("Task name: "))
        add_task(task=task_user, todo_list=list_task)
        print("")
        
    elif user_choose == 1:
        system("clear")
        remove_last_task(list_remove=list_task, list_add= backup_task_list)
        
    elif user_choose == 2:
        system("clear")
        remove_last_task(list_remove=backup_task_list, list_add= list_task)
    
    elif user_choose == 3:
        system("clear")
        print("TO DO LIST")
        for _index, task in enumerate(list_task):
            print("{}. {}".format(_index+1,task))
        print("")
    