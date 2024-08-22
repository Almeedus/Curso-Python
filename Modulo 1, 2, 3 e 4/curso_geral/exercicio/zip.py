cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
sigla_estado = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    intervaloMax = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervaloMax)
    ]

print(zipper(cidades, sigla_estado))
print(list(zip(cidades, sigla_estado)))