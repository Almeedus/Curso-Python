import json

person = {
    "name": "Eduardo",
    "middle_name": "Almeida",
    "address": [
        {"street": "Avenida Nestor Fogaça", "number": 1017},
        {"street": "Rua Franscisco Rosa", "number": 71},
    ],
    "height": 1.83,
    "preferred_numbers": (7,14,9,20),
    "dev": True,
    "nothing": None
}

file_path = "C:\\Users\\eduar\\OneDrive\\Documentos\\Curso-Python\\Modulo 1, 2, 3 e 4\\revisao\\json_python\\json_exemple.json"

# Carregando as informações para dentro do json
with open(file_path, "w", encoding='utf8') as file:
    # jogar o objeto dentro do arquivo
    json.dump(
        person, file, 
        # ensure_ascii= False é para desabilitar o caractere em ASCII
        ensure_ascii= False,
        # indentação == 2 é utlozado para formatar o arquivo 
        indent= 2
    )
    

#abrindo o arquivo
with open (file_path, 'r', encoding='utf8') as file:
    #salvar o que está no arquivo json em uma variável
    second_person = json.load(file)
    
print(second_person['name'])