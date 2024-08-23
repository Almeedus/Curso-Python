nome = input('Informe seu nome: ')

try:
    tamanho_nome = len(nome)

    nome_curto = tamanho_nome <= 4
    nome_normal = tamanho_nome >= 5 or tamanho_nome == 6
    nome_grande = tamanho_nome >= 7

    if nome_curto == 1:
        print('Nome curto')
        print(f'O nome: {nome.upper()} possui {tamanho_nome} letras')
    elif nome_normal == 1:
        print('Nome normal')
        print(f'O nome: {nome.upper()} possui {tamanho_nome} letras')
    elif nome_grande == 1:
        print('Nome grande')
        print(f'O nome: {nome.upper()} possui {tamanho_nome} letras')

except:
    print('O valor digitado é invalido')