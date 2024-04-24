from itertools import groupby

#groupby - agrupamento de valores (itertools)
#o groupby precisa que os valores estejam ordenados para conseguir agrupar 
#exemplo: ['a','a','a','b','b','c']
#caso estejam fora de ordem, ele irá criar uma outra chave para agrupar
#métodos de ordenação, sorted() ou .sort

alunos = [
    {'aluno':'Eduardo', 'nota':10},
    {'aluno':'Julio', 'nota':2},
    {'aluno':'João', 'nota':10},
    {'aluno':'Bianca', 'nota':7},
    {'aluno':'Bruna', 'nota':6},
    {'aluno':'Carol', 'nota':7}, 
]

#como usamos o lambda duas vezes e ele é uma função que recebe um aluno sendo 'a'
#e retorna o valor da chave 'nota' desse aluno, vamos criar uma função
#para assim não repetir código
def ordena(aluno):
    return aluno['nota']

#Vamos ordenar o dicionário para fazer o agrupamento

alunos_agrupados = sorted(alunos, key= ordena, reverse=True)



#ao fazer esse groupby é retornado um iterator
grupos = groupby(alunos_agrupados, key= ordena)

# #então para conseguir ver os valores que são retornados precisamos transformá-los em uma lista
# #note que é retornado o valor e o valor do grupo que está sendo utilizado para agrupar(que é um iterator)
# #print(list(grupos))

# #para melhor visualização, podemos utilizar de um for antes do print
for chave,grupo in grupos:
    print(chave)

    #por ser um iterator, eu posso utilizar um list() para verificar o que tem deste agrupamento
    #print(list(grupo))

    for aluno in grupo:
        print(aluno)