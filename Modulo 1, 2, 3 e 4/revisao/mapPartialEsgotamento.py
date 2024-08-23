#Map, partial, GeneratorType e esgotamento de iterators
from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep ='\n')
    print()
    

produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 22.32},
    {'nome': 'Produto 5', 'preco': 10.11},
    {'nome': 'Produto 4', 'preco': 105.87},
    {'nome': 'Produto 3', 'preco': 69.90}
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

#List comprehention
#novos_produtos = [
#    {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# ]

# ===============================================================================

def muda_preco_produtos(produto):
    return {
        **produto, 
        'preco': aumentar_dez_porcento(produto['preco'])
    }
    
#map - ele vai passar cada um dos produtos da lista na função passada
novos_produtos = map(
    muda_preco_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
