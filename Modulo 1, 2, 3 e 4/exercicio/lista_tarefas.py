from os import system
# Lista de tarefas: Fazer e desfazer ações

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'Caminhar'] -> Adicionar fazer caminhar
def add_task(task=str, todo_list=None):
    if todo_list is None:
        todo_list = []
        
    todo_list.append(task)
    return todo_list

# desfazer = ['fazer café'] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']

# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


while True:
    print("To-do list:")
    print("Add task - Undo task - Redo task")
    
    try:
        user_choose = input("USER-TYPE: ")
        user_choose = str(user_choose).strip().capitalize()
        
    except ValueError:
        _red = ["\033[31m","\033[m"]
        print(_red[0],"Wrong value! Type only text.",_red[1])
        input("Type enter to reload.")
        system("clear")
        continue
    
    
    
    