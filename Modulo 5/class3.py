# Atributo de classe
# __dict__ e vars para atributos de instancia

class Pessoa: 
    ano_atual = 2025
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa("Lucas", 23)
print(p1.get_ano_nascimento())

#Onde é salvo todos os dados da instancia
print(p1.__dict__)
print(vars(p1))