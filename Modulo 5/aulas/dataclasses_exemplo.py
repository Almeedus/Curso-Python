# O que são?
# módulo que fornece um decorador e funções para criar métodos como: 
# __init__(), __repr() e __eq__() 

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str | None = None
    sobrenome: str | None = None
    idade: int | None = None

    @property
    def nome_completo(self) -> str:
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, nome: str) -> None:
        nome, *sobrenome = nome.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa()
    p1.nome_completo = 'Lala lele lili lolo'
    print(p1.nome_completo)