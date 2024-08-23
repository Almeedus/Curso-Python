# Modo de manipulação
# (r) leitura - (w) escrita - (x) criação - (a) escreve ao final do arquivo
# (b) binário - (t) texto - (+) leitura e escrita

from criando_arquivos import caminho_completo 

with open(caminho_completo, 'w+') as arquivo:
    # Para escrever trabalhamos com o arquivo.write()
    # Escrevendo apenas uma linha por vez
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    
    # Escrevendo várias linhas por vez
    arquivo.writelines(
        # Enviando uma tupla - vários dados para serem escritos -
        ('Linha 3\n','Linha 4\n','Linha 5\n')
    )
    
    # Note que ao fazer a leitura no mesmo Context Manager precisamos subir o 'cursor do python' para cima
    # uma vez que ele escreveu as linhas e está abaixo do que está escrito
    # caso realize a leitura assimn o output será vazio. Para mudar isso usamos a função .seek() que joga o cursor para o topo do arquivo
    arquivo.seek(0,0)
    
    # Para ler o arquivo usamos o '+' no parametro acima e a função read()
    linhas = arquivo.read()
    print(linhas)

# Outra forma de realizar a leitura é iniciando um novo Context Manager
with open(caminho_completo, 'r') as arquivo:
    # Para ler linha por linha usamos o arquivo.readline()
    # por conta da quebra de linha adicionada, ao realizar o readline() ele pula uma linha no output
    # para resovler isso podemos usar o parametro end=''
    # basicamente o readline funciona como um 'next', onde ele lerá a linha 1 e parará na linha seguinte até acabar o conteúdo
    print(arquivo.readline(),end='')
    # Podemos usar a função strip que remove os espaços em branco do inicio e do final
    print(arquivo.readline().strip())
    print()
    
    # Aqui é retornado uma lista que precisa ser tratada
    arquivo.seek(0,0)
    for l in arquivo.readlines(): print(l, end='')
    
    