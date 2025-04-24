class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def saudacao(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
    
p1 = Pessoa(nome='Lucas', idade=20, cpf='123.456.789-00')
p2 = Pessoa(nome='Ana', idade=25, cpf='987.654.321-00')


print(f'Nome: {p1.nome}, Idade: {p1.idade}, CPF: {p1.cpf}')
p1.saudacao()
print()
print(f'Nome: {p2.nome}, Idade: {p2.idade}, CPF: {p2.cpf}')
p2.saudacao()