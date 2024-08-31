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

