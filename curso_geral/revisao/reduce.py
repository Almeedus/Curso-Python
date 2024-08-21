# Reduce - faz a redução de um iteravel em um valor

# Para utilizar precisamos importar da biblioteca 'functools'
from functools import reduce

produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 22.32},
    {'nome': 'Produto 5', 'preco': 10.11},
    {'nome': 'Produto 4', 'preco': 105.87},
    {'nome': 'Produto 3', 'preco': 69.90}
]

def funcao_reduce(acumulador, produto):
    return acumulador + produto['preco']


# Primeiro parametro é uma função,
# Segundo parametro é o iteravel
# terceiro valor é o valor inicial
total = reduce(
    funcao_reduce,
    produtos,
    0
)
print(total)