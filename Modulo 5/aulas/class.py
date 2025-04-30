class Carro:
    def __init__(self, marca, modelo, cor, ano, tipo):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.tipo = tipo
        
    def acelerar(self):
        print(f'O carro {self.modelo} está acelerando.')
        
fusca = Carro('Volkswagen', 'Fusca', 'azul', 1970, 'gasolina')
fusca.acelerar()