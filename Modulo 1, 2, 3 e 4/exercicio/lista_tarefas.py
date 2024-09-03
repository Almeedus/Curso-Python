from os import system

def add_task(task=str, todo_list=None):
    if todo_list is None:
        todo_list = []
    todo_list.append(task)
    return todo_list

list_task = []
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
        _red = ["\033[31m","\033[m"]
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
        # desfazer = ['fazer café'] -> Refazer ['caminhar']
        # desfazer = [] -> Refazer ['caminhar', 'fazer café']
        system("clear")
        input("enter under task")
        
    elif user_choose == 2:
        # refazer = todo ['fazer café']
        # refazer = todo ['fazer café', 'caminhar']
        system("clear")
        input("enter redo task")
    
    elif user_choose == 3:
        system("clear")
        print("TO DO LIST")
        for _index, task in enumerate(list_task):
            print("{}. {}".format(_index+1,task))
        print("")
    