#função de uma linha
#list = [4,12,32,1,6,3]

list = [ 
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Almeida'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#passando o nome da função para configurar o sort
def ordena_nome (item):
    return item['nome']

#def ordena_sobrenome (item):
#    return item['sobrenome']

print('ORDENAÇÃO POR NOME:')
list.sort(key=ordena_nome)
for item in list:
    print(item)

print()

print('ORDENAÇÃO POR SOBRENOME:')
#exemplo de função lambda (função em uma linha só)
list2 = sorted(list , key=lambda item: item['sobrenome'])
for item in list2:
    print(item)