from functools import partial

#map - usado para mapear dados

#MAP FILTER AND REDUCE

def print_iter(iterator):
    #estou pegando o iterador de cada dicionário da lista passada e pegando seu valor
    #ao pegar o iterator se tem o valor da variavel e seu valor de iterator (um código estranho kkk)
    #quando usado o método list eu consigo listar os valores dessas variáveis
    #e se usar o '*', aplico para toda a lista de produtos
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.00},
    {'nome': 'Produto 3', 'preco': 10.50},
    {'nome': 'Produto 2', 'preco': 105.00},
    {'nome': 'Produto 4', 'preco': 69.90},
]


#Função para aumentar o preço de todos os produtos da lista na porcentagem desejada
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

#usando o método partial para aumentar a porcentagem dos produtos em 10%
aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

#criando uma variavel a partir de um for e salvando todos os dados nela
# o ** antes do p significa que estamos desempacotando todas as chaves e valores do item p que está na lista produtos
#na linha 38 estamos pegando a chave preço e alterando o valor da sua chave em 10% para enfim salvar
"""
novos_produtos = [
    {**p,
     'preco': aumentar_dez_porcento(p['preco'])}
     for p in produtos
]
"""

#essa função faz exatamente a mesma coisa da função de cima
def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco']
        )
    } 
    

#a função map do python precisa que seja passada outra função como parametro, no caso vamos criar ela anteriormente
novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

#o funcionamento desta função está detalhada no seu escopo interno
print_iter(produtos)

print_iter(novos_produtos)