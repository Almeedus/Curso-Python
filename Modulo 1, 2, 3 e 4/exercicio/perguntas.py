perguntas = [
    {
        'pergunta': 'Quantos é 5x5?',
        'opcao' : [25,20,50,40],
        'certa' : 25
    },
    {
        'pergunta': 'Quem foi Roberto Carlos?',
        'opcao': ['Corredor de F1', 'Cantor', 'Escritor', 'Lutador'],
        'certa': 'Cantor'
    }
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['pergunta'])
    print()

    opcoes = pergunta['opcao']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')
    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == pergunta['certa']:
                    acertou = True
        
        if acertou:
            print('Acertou')
            qtd_acertos += 1
        else:
            print('Errou')

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
print()