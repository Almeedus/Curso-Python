#list comprehension em py
#list comprehension é uma forma rapida de criar listas a artir de iteráveis

lista2 = []
for numero in range(10):
    lista2.append(numero)
print(lista2)

lista = [
    numero * 2
    for numero in range(10)
    ]
print(lista)