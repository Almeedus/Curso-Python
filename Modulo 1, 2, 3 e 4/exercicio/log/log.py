from datetime import datetime
from random import randint
from time import sleep



# Configuração do caminho de salvamento
caminho_arquivo = 'C:\\Users\\eduar\\OneDrive\\Documentos\\Curso-Python\\Modulo 1, 2, 3 e 4\\curso_geral\\exercicio\\log\\'
nome_arquivo = 'log.txt'
caminho_completo = caminho_arquivo + nome_arquivo

# Obtendo a hora em tempo real
data = datetime.now()

# Manipulando a hora em tempo real
def formatar_hora(data_recebida=datetime):
    hora_formatada = f'[{data_recebida.day}-{data_recebida.month}-{data_recebida.year} {data_recebida.hour}:{data_recebida.minute}:{data_recebida.second}]'
    return hora_formatada

# Criando dados aleatórios para inserir
def dados_aleatorios():
    dado = randint(1,1000)
    return dado

# Criando a linha organizada para inserir no txt
def organizando_entrada():
    relogio = formatar_hora(data)
    dado = dados_aleatorios()
    
    return f'{relogio}  Dados do sensor: {dado}.\n'


# Iniciando um loop eterno 
while True:
    
    # Inserindo no arquivo as informações
    with open(caminho_completo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(organizando_entrada())
    sleep(60)