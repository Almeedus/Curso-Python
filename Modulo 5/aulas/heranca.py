#Herança

#Classe principal (Pessoa)
#Super class    Base class    Parent class
#Classe filha (Aluno)
#Sub class    Child class    Derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome(self):
        return f'meu nome é {self.nome} {self.sobrenome}'
        
        
class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, sala):
        super().__init__(nome, sobrenome)
        self.sala = sala
    
    def falar_nome(self):
        return super().falar_nome() + f' e estudo no {self.sala}'
    
aluno1 = Aluno('Eduardo','Almeida','3ano b')
print(aluno1.falar_nome())



# Herança Multipla 
# As classes podem herdar de mais de uma classe

# Mixing
# Misturando classes de 'famílias diferentes' (colocar uma classe que não tem nada haver)

# MRO - Método de Resolução de Métodos (Method Resolution Order)
# O método mro() ou o atributo __mro__, fornece a ordem de procedencia dos métodos

