# Modo de abertura de arquivo e encoding com with open
# Enconding - ascentos, espaços, caracteres especiais que podem me causar problemas

# Modo de manipulação
# (r) leitura - (w) escrita - (x) criação - (a) escreve ao final do arquivo
# (b) binário - (t) texto - (+) leitura e escrita

from criando_arquivos import caminho_completo 

# Para usarmos caracteres especiais e acentos utilizamos o parametro para o open - encoding= 'utf-8'
with open(caminho_completo,'a', encoding= 'utf-8') as arquivo:
    arquivo.write('Atenção')