"""
Exibe os indices da lista
0 nome
1 nome
2 nome
"""
lista = ['Eduardo', 'Maria', 'Clara']

print('Lista de nomes:')
for nome in lista:
    print(lista.index(nome), '-', nome)

lista.append('Almeida')
print('='*20)

print('Nova lista:')
for nome in lista:
    print(lista.index(nome), '-', nome)

