frase = 'O Python é uma linguagem de programação' \
    ' multiparadigma. ' \
    'Python foi criado por Guido Van Rossum'

i = 0 
letra_atual = ''
letras_contadas = 0

qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_Vezes = ''

frase_tratada = frase.strip()

while i < len(frase):
    
    letra_atual = frase[i]
    letras_contadas = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < letras_contadas:
        ...
    
    print(f'{letra_atual} - {letras_contadas}')
    i += 1