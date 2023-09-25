#Empacotamento e desempacotamento de dicionarios
a,b = 1,2
a,b = b,a
#print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

#args e kargs
# a,b = pessoa.items() #retorna uma tupla
# print("retorna uma tupla: ", a,b)
# a,b = pessoa.values() #retorna o valor
# print("retorna o valor: ",a,b)
# a,b = pessoa # retorna a chave
# print("retorna a chave: ",a,b)
# print()
# (a1,a2), (b1,b2) = pessoa.items()
# print(f"{a1.capitalize()}: {a2}")
# print(f"{b1.capitalize()}: {b2}")

pessoa_completa = {}
pessoa_completa = {**pessoa, **dados_pessoa}

#args (ja visto)
# for chave,item in pessoa_completa.items():
#     print(f"{chave.capitalize()}: {item}")

#kwargs - keywords arguments (argumentos nomeados)
def showArguments(*args, **kwargs):
    for chave,item in pessoa_completa.items():
        print(f"{chave.capitalize()}: {item}")

showArguments(**pessoa_completa)