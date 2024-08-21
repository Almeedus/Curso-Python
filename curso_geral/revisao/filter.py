# filter é um filtro funcional
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

# O que ocorre aqui, que é quando ele usa a comprensão de lista para apenas
# os valores maiores que 10
#novos_produtos = [
#    p for p in produtos
#    if p['preco'] > 10 
#]

# ===============================================================================

# Usando a função filter
# primeiro parametro é uma função, no caso usamos uma 'função lambda'
# segundo parametro é o iterado, ou seja, onde será realizado a função anterior
novos_produtos = filter(
    lambda p: p['preco'] > 20,
    produtos 
)

print_iter(produtos)
print_iter(novos_produtos)