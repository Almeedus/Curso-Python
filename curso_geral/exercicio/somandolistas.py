l1 = [1,2,3,4,5,6]
l2 = [9,8,7,]

def somaLista (l1, l2):
    intervaloMax = min(len(l1), len(l2))

    listaSomada = [
        (l1[i]+ l2[i]) for i in range(intervaloMax)
    ]

    return listaSomada

print(somaLista(l1,l2))