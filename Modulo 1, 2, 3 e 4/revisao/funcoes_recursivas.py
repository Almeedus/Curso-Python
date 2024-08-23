# Funções recursivas, recursividade e Stack OverFlow

# Basicamente uma função recursiva é uma função que chama ela mesma dentro do seu escopo

# O que uma função recursiva deve ter?
# 1. Problemas que possa ser divido em partes menores
# 2. Um caso recursivo que resolve o pequeno problema
# 3. Um caso base que para a recursão
# Exemplo: Fatorização - n! = 5 * 4 * 3 * 2 * 1 = 120

# Exercicio: contar de 1 até 10
def recursiva(inicio=0, fim=10):
    # Caso base - SEGURANÇA - para não ter o stack overflow
    if inicio >= fim:
        return fim
    
    # Função recursiva
    inicio += 1
    return recursiva(inicio, fim)
    
recursiva()
    
    
# Exercicio: Fatorial
def fatorial(numero):
    if numero <= 1: return 1
    
    return numero * fatorial(numero - 1)

# Utilizando uma função recursiva no limite permitido sem a alteração
# o resultado é GIGANTE uahsuhasu
print(fatorial(996))