numero = input("Irei dobrar seu numero: ")

try:
    numero_float = float(numero)
    print(f"O dobro de {numero} é {numero_float*2}")

except:
    print("O que foi digitado não é um número")