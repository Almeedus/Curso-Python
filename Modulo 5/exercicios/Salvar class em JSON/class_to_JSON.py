import datetime
import json

PATH ='C:\\Users\\eduar\\Documents\\Curso-Python\\Modulo 5\\exercicios\\Salvar class em JSON\\pessoa.json'
class Pessoa:
    ANO_ATUAL = datetime.datetime.now().year
    
    def __init__ (self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def ano_nascimento(self):
        return self.ANO_ATUAL - self.idade
        
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def get_cpf(self):
        return self.cpf
    
p1 = Pessoa('Lucas', 23, '123.456.789-00')

dados = p1.__dict__


def fazer_dump():
    with open(PATH, "w", encoding='utf8') as file:
        json.dump(
            dados,file,
            ensure_ascii=False,
            indent=2
        )
    
if __name__ == '__main__':
    fazer_dump()