#adiando execução de funções

def soma(x,y):
    return x+y

def multiplica(x,y):
    return x*y


#Essa função dentro de uma outra função se chama CLOSURE
#Básicamente ela adia a função
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna


soma_cinco = criar_funcao(soma, 5)
multiplica_por10 =criar_funcao(multiplica, 10)

print(soma_cinco(10))
print(multiplica_por10(10))