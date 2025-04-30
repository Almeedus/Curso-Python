import json
from class_to_JSON import Pessoa, PATH


with open(PATH, "r", encoding='utf8') as file:
    dados = json.load(file)
    
    p2 = Pessoa(str(dados['nome']), int(dados['idade']), str(dados['cpf']))

    
print(f'Nome: {p2.get_nome()}')
print(f'Idade: {p2.get_idade()}')
print(f'CPF: {p2.get_cpf()}')
print(f'Ano de Nascimento: {p2.ano_nascimento()}')