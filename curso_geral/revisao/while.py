print("Temporizador")
tempo = input('Informe um valor inteiro: ')

try:
    tempo_segundos = int(tempo)

    contador = tempo_segundos
    while contador >= 1:
        print(contador,end='-')
        contador -= 1
    
    print('0')
    print('\nTerminou!')
except:
    print('\nValor inválido')
