# Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome
        sexo = ''
        self.alimentado = False
        
    def definir_sexo(self, sexo):
        self.sexo = sexo
        
    def retornando_animal(self):
        return f"Nome: {self.nome}, Sexo: {self.sexo}"
    
    def comendo(self, comida):
        self.alimentado = True
        return f"{self.nome} está comendo {comida}"
        
    
    
        

cachorro = Animal(nome = "Rex")
cachorro.definir_sexo("Macho")
#print(cachorro.retornando_animal())

gato = Animal(nome="Mimi")
gato.definir_sexo("Fêmea")
gato.comendo("ração")
#print(gato.retornando_animal())

print(f'{cachorro.nome} comeu: {"Sim" if cachorro.alimentado else "Não"}')
print(f'{gato.nome} comeu: {"Sim" if gato.alimentado else "Não"}')