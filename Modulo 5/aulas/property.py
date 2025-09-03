# O property é um getter no modo Pythonico

# Básicamente um getter é um método usado para obter atributo
# Modo pythonico é como acontece no python

# A @property é uma propriedade de objeto que se comporta como um atributo


#Usada em algumas situações:
"""
1. como um getter
2. para evitar quebrar o código cliente (código que usa o seu código)
3. para habilitar um setter
4. para executar ações ao obter um atributo
"""

#código em si
class Caneta:
    def __init__(self, cor):
        # argumentos que tenham _ ou __
        #não devem ser usados fora da classe
        self._cor = cor

    @property
    def cor(self):
        return self._cor


    @cor.setter
    def cor(self, cor):
        self._cor = cor
    



# código cliente 
caneta2 = Caneta
caneta = Caneta('Azul')
caneta2.cor = 'Rosa'

# getter -> obtendo o valor 
print(caneta.cor)
print(caneta2.cor)

