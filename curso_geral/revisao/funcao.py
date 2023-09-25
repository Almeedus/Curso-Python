#como criar sua propria função em Python

"""
def Print(variavel):
    print(variavel)

pergunta = input('O que deseja mostrar: ')
Print(pergunta)
"""

#argumento nomeado e nao nomeado(posicional)

"""
def soma(x, y): #<- parametros
    print(f'{x=} + {y=} = {x + y}')

soma(2, 2) #<- argumentos posicionais (nao noemado)
soma(y=2, x=1) #<- argumentos nomeados
"""

#Valores padrões
#refatoração de código : editar o código
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=} = {x + y + z}')
    else:
        print(f'{x=} + {y=} = {x + y}')

soma(2, 2, 2) 
soma(y=2, x=1) 