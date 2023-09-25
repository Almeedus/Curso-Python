def criar_funcao(numero:int):
    def multiplicar(*args):
        numeros_multiplicados = []
        for numeros in args:
            numeros_multiplicados.append(numeros * numero)
        return numeros_multiplicados
    return multiplicar

multiplicacao = criar_funcao(3)
print(multiplicacao(1,2,3,4,5))