class Fabricante:
    def __init__(self, nome):
        self._nome = nome
    
    
class Motor:
    def __init__(self, nome):
        self._nome = nome


class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._nome_motor = None
        self._nome_fabricante = None
    
    def getter_carro(self):
        return {
            'nome': self._nome, 
            'motor': self._nome_motor._nome, 
            'fabricante' : self._nome_fabricante._nome
        }
    
    @property
    def motor(self):
        return self._nome_motor._nome
    
    @motor.setter
    def motor(self, nome_motor):
        self._nome_motor = nome_motor
        
    @property
    def fabricante(self):
        return self._nome_fabricante._nome

    @fabricante.setter
    def fabricante(self, nome_fabricante):
        self._nome_fabricante = nome_fabricante

# Criando objetos e testando a classe

honda = Fabricante('Honda')
motor = Motor('2.1')

carro1 = Carro('celta')
carro1.motor = motor
carro1.fabricante = honda

carro2 = Carro('uno')
carro2.motor = motor
carro2.fabricante = honda

honda.carro = carro1
honda.carro = carro2

print(carro1.getter_carro())
print(carro2.getter_carro())