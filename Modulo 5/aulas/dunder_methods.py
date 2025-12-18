#dunder, magic ou special métodos
#são métodos do python 
# dunder = métodos que contém __ (dois underscore no começo e no final)

# SEMPRE QUE FOR USAR UM SPECIAL METHODS É NECESSÁRIO SABER A ASSINATURA DO MÉTODO

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z


    # usar para retornar APENAS uma string do objeto
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


    # usar para comunicação com desenvolvedores
    def __repr__(self):
        #class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}|y={self.y!r}|z={self.z!r})'



p1 = Ponto(1,2)
p2 = Ponto(3,4)

print(p1, p2, '\n')

print(f'Chamando como string: {p2!s}')
print(f'Chamando como repr: {p2!r} \n')

print(repr(p2))
