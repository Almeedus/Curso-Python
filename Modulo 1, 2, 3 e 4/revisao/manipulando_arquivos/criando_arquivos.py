# Manipulação de arquivo com python

# O caminho refere ao caminho que estou quando não especifico onde ele deve ser aberto
# pelo fato do python ter dificuldade em entender a barra invertida no caminho, utilizamos duas barras ao inves de uma
caminho_completo = 'C:\\Users\\eduar\\OneDrive\\Documentos\\Curso-Python\\Modulo 1, 2, 3 e 4\\curso_geral\\revisao\\criando_arquivo\\'
caminho_arquivo = 'arquivo.txt'

# Concatenando o arquivo para que ele fique com o caminho completo e com o arquivo, dessa forma podendo ser achado dentro do
# diretório
caminho_completo += caminho_arquivo

# Aqui o arquivo não existe, não o criamos, apenas escrevemos um caminho no qual ele pode estar (ou deve estar)
# print('SAIDA:', caminho_completo)

# ================================================================================================================================

# Modo de manipulação
# (r) leitura - (w) escrita - (x) criação - (a) escreve ao final do arquivo
# (b) binário - (t) texto - (+) leitura e escrita

# Criação de um arquivo
# Com o caminho completo e o modo de manipulação podemos criar um arquivo
# Somente criação (x)    -       Criação e inserção de dados (w)
#
# arquivo = open(caminho_completo, 'w')
# arquivo.close()

# ================================================================================================================================
# Context manager - responsável por abrir e fechar de forma automática quando se tem os métodos open() e close()
# para utilizar dessa funcionalidade, usamos o WITH função que abre 'open()', seguido de AS e o 'nome do arquivo
with open(caminho_completo, 'w') as arquivo:
    ...
