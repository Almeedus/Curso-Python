#             Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro
# receberemos a própria classe.

class Pessoa:
    ano = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_pessoa(cls, nome, idade):
        return cls(nome, idade)
    
    def apresentacao_pessoa(self):
        print(f'{self.nome} tem {self.idade} anos.')