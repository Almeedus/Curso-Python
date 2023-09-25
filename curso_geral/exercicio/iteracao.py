#Iterando strings com while

nome = input('Informe um nome: ')

tamanho_nome = 0

while tamanho_nome >= len(nome):
    print(f'{nome[tamanho_nome]}',sep='*')
    tamanho_nome +=1 