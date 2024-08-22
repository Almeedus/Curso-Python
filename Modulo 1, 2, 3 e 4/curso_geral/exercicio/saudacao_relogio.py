hora_atual = input('Que horas são? Ex.: 10:30 \nDigite um valor: ')

try:
    hora_convertida = int(hora_atual[0:1])

    bom_dia = hora_convertida <= 00 or hora_convertida >= 11
    boa_tarde = hora_convertida <= 12 or hora_convertida >= 17
    boa_noite = hora_convertida <= 18 or hora_convertida >= 23

    if bom_dia == 1:
        print(f'Bom dia')
    elif boa_tarde == 1:
        print(f'Boa tarde')
    elif boa_noite == 1:
        print(f'Boa noite')

except:
    print('O valor digitado não é valido')