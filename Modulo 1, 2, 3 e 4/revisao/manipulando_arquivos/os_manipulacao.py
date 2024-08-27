# or.remove (removendo), os.unlink (removendo), os.rename(renomeando)
# Utilização da biblioteca OS que utiliza do sistema operacional para realizar os comandos.

import os
from escrevendo_arquivo import caminho_completo

caminho_velho = 'C:\\Users\\eduar\\OneDrive\\Documentos\\Curso-Python\\arquivo2.txt'
caminho_novo = 'C:\\Users\\eduar\\OneDrive\\Documentos\\Curso-Python\\Modulo 1, 2, 3 e 4\\revisao\\manipulando_arquivos\\arquivo2.txt'

# Apagar o arquivo
"os.remove(arquivo)"
"os.unlink(arquivo)"

# Renomear ou mover o arquivo
"os.rename"

# Renomeando o arquivo
# No caso de não especificar o caminho no nome a ser renomeado, ele salva no diretório atual que está sendo rodado o programa python
print('\n\nTERMINAL OUTPUT: Renomeado')
os.rename(caminho_completo, 'arquivo2.txt')

# Movendo o arquivo
print('TERMINAL OUTPUT: Movido')
os.rename(caminho_velho, caminho_novo)

# Apagar um arquivo
print('TERMINAL OUTPUT: Apagado')
os.remove(caminho_novo)