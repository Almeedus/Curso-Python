numero = input('Informe um número: ')

try:
    numero_digitado = float(numero)

    if numero_digitado % 2 == 0:
        print(f'O {numero} é par')
    else:
        print(f'O {numero} é impar')
except:
    print(f'Valor digitado: {numero.upper()} não é válido')